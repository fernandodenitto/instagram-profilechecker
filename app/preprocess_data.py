import json
import os
import csv
import statistics
from scipy.stats import skew 
import pandas

def emptyPicProfileFromURL(picProfileURL):

    """ Check if the URL of the Profile Pic contains the substring 
        "44884218_345707102882519_2446069589734326272_n.jpg" that is
        the name of the file that Instagram use for the emplty photo profile.
        The function returns true if the Profile Picture is not present, false otherwise.
    """

    emptyPicURL="44884218_345707102882519_2446069589734326272_n.jpg"

    return (emptyPicURL in picProfileURL)

def GenerateData(ProfileData):
    

    # Profile picture present
    profilepic = False if emptyPicProfileFromURL(ProfileData["profile_pic_url"]) else True
    # Biography present
    bio = 0 if ProfileData["biography"] == "" else len(ProfileData["biography"])
    # Follows count
    follow = ProfileData["follows_count"]
    # Followed by count
    followed = ProfileData["followed_by_count"]
   
    # Follower/Followed ratio
    if follow == 0:
        ffratio = followed/(follow + 1)
    else:
        ffratio = followed/follow 
    
    # Media count
    medias = ProfileData["media_count"]
    # Private
    private = ProfileData["is_private"]
    # Verified
    verified = ProfileData["is_verified"]
    # Is Business Account
    business = ProfileData["is_business_account"]
    # Is Joined recently
    joined = ProfileData["is_joined_recently"]
    # Highlight reel count
    highlights = ProfileData["highlight_reel_count"]

    item = [[profilepic, bio, follow, followed, ffratio, medias, private, verified, business, joined, highlights]]
    
    return item




      












