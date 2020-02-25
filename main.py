#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import codecs
import configparser
import errno
import glob
from operator import itemgetter
import json
import logging.config
import hashlib
import os
import pickle
import re
import sys
import textwrap
import time
import csv
from time import sleep


try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import warnings

import threading
import concurrent.futures
import requests
import tqdm

from instagram_scraper.constants import *
from scrapers.posts.instagram_scraper import *
from scrapers.profile.igramscraper.instagram import Instagram
from preprocess_data import *



def main():
    parser = argparse.ArgumentParser(
        description="instagram-scraper scrapes and downloads an instagram user's photos and videos.",
        epilog=textwrap.dedent("""
        You can hide your credentials from the history, by reading your
        username from a local file:

        $ instagram-scraper @insta_args.txt user_to_scrape

        with insta_args.txt looking like this:
        -u=my_username
        -p=my_password

        You can add all arguments you want to that file, just remember to have
        one argument per line.

        Customize filename:
        by adding option --template or -T
        Default is: {urlname}
        And there are some option:
        {username}: Instagram user(s) to scrape.
        {shortcode}: post shortcode, but profile_pic and story are none.
        {urlname}: filename form url.
        {mediatype}: type of media.
        {datetime}: date and time that photo/video post on,
                     format is: 20180101 01h01m01s
        {date}: date that photo/video post on,
                 format is: 20180101
        {year}: format is: 2018
        {month}: format is: 01-12
        {day}: format is: 01-31
        {h}: hour, format is: 00-23h
        {m}: minute, format is 00-59m
        {s}: second, format is 00-59s

        """),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        fromfile_prefix_chars='@')

    parser.add_argument('username', help='Instagram user(s) to scrape', nargs='*')
    parser.add_argument('--destination', '-d', default='./users', help='Download destination')
    parser.add_argument('--login-user', '--login_user', '-u', default=None, help='Instagram login user')
    parser.add_argument('--login-pass', '--login_pass', '-p', default=None, help='Instagram login password')
    parser.add_argument('--followings-input', '--followings_input', action='store_true', default=False,
                        help='Compile list of profiles followed by login-user to use as input')
    parser.add_argument('--followings-output', '--followings_output', help='Output followings-input to file in destination')
    parser.add_argument('--filename', '-f', help='Path to a file containing a list of users to scrape')
    parser.add_argument('--quiet', '-q', default=False, action='store_true', help='Be quiet while scraping')
    parser.add_argument('--maximum', '-m', type=int, default=50, help='Maximum number of items to scrape')
    parser.add_argument('--retain-username', '--retain_username', '-n', action='store_true', default=False,
                        help='Creates username subdirectory when destination flag is set')
    parser.add_argument('--media-metadata', '--media_metadata', action='store_true', default=True,
                        help='Save media metadata to json file')
    parser.add_argument('--profile-metadata', '--profile_metadata', action='store_true', default=False,
                        help='Save profile metadata to json file')
    parser.add_argument('--proxies', default={}, help='Maximum number of items to scrape')
    parser.add_argument('--include-location', '--include_location', action='store_true', default=False,
                        help='Include location data when saving media metadata')
    parser.add_argument('--media-types', '--media_types', '-t', nargs='+', default='none',
                        help='Specify media types to scrape')
    parser.add_argument('--latest', action='store_true', default=False, help='Scrape new media since the last scrape')
    parser.add_argument('--latest-stamps', '--latest_stamps', default=None,
                        help='Scrape new media since timestamps by user in specified file')
    parser.add_argument('--cookiejar', '--cookierjar', default=None,
                        help='File in which to store cookies so that they can be reused between runs.')
    parser.add_argument('--tag', action='store_true', default=False, help='Scrape media using a hashtag')
    parser.add_argument('--filter', default=None, help='Filter by tags in user posts', nargs='*')
    parser.add_argument('--location', action='store_true', default=False, help='Scrape media using a location-id')
    parser.add_argument('--search-location', action='store_true', default=False, help='Search for locations by name')
    parser.add_argument('--comments', action='store_true', default=False, help='Save post comments to json file')
    parser.add_argument('--no-check-certificate', action='store_true', default=False, help='Do not use ssl on transaction')
    parser.add_argument('--interactive', '-i', action='store_true', default=False,
                        help='Enable interactive login challenge solving')
    parser.add_argument('--retry-forever', action='store_true', default=False,
                        help='Retry download attempts endlessly when errors are received')
    parser.add_argument('--verbose', '-v', type=int, default=0, help='Logging verbosity level')
    parser.add_argument('--template', '-T', type=str, default='{urlname}', help='Customize filename template')
    parser.add_argument('--log_destination', '-l', type=str, default='./log', help='destination folder for the instagram-scraper.log file')

    args = parser.parse_args()

    if (args.login_user and args.login_pass is None) or (args.login_user is None and args.login_pass):
        parser.print_help()
        raise ValueError('Must provide login user AND password')

    if not args.username and args.filename is None and not args.followings_input:
        parser.print_help()
        raise ValueError('Must provide username(s) OR a file containing a list of username(s) OR pass --followings-input')
    elif (args.username and args.filename) or (args.username and args.followings_input) or (args.filename and args.followings_input):
        parser.print_help()
        raise ValueError('Must provide only one of the following: username(s) OR a filename containing username(s) OR --followings-input')

    if args.tag and args.location:
        parser.print_help()
        raise ValueError('Must provide only one of the following: hashtag OR location')

    if args.tag and args.filter:
        parser.print_help()
        raise ValueError('Filters apply to user posts')

    if args.filename:
        args.usernames = InstagramScraper.parse_file_usernames(args.filename)
    else:
        args.usernames = InstagramScraper.parse_delimited_str(','.join(args.username))

    if args.media_types and len(args.media_types) == 1 and re.compile(r'[,;\s]+').findall(args.media_types[0]):
        args.media_types = InstagramScraper.parse_delimited_str(args.media_types[0])

    if args.retry_forever:
        global MAX_RETRIES
        MAX_RETRIES = sys.maxsize

    

    scraper = InstagramScraper(**vars(args))

    if args.login_user and args.login_pass:
        scraper.authenticate_with_login()
    else:
        scraper.authenticate_as_guest()

    if args.followings_input:
        scraper.usernames = list(scraper.query_followings_gen(scraper.login_user))
        if args.followings_output:
            with open(scraper.destination+scraper.followings_output, 'w') as file:
                for username in scraper.usernames:
                    file.write(username + "\n")
            # If not requesting anything else, exit
            if args.media_types == ['none'] and args.media_metadata is False:
                scraper.logout()
                return

    if args.tag:
        scraper.scrape_hashtag()
    elif args.location:
        scraper.scrape_location()
    elif args.search_location:
        scraper.search_locations()
    else:
        scraper.scrape()

    scraper.save_cookies()

    username = sys.argv[1]
    instagram = Instagram()
    instagram.with_credentials('donatella.marchese.7', 'vietatofumare')
    instagram.login()
    sleep(2) # Delay to mimic user
    account = instagram.get_account(username)
    
    ProfileData = account.__dict__

    item = GenerateData(ProfileData)
    

    with open('UserData.json', 'w') as outfile:
        json.dump(item, outfile, indent=4)

    

    
    
    









if __name__ == '__main__':
    main()
