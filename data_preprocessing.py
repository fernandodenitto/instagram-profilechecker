import json
import os
import csv
import statistics
from scipy.stats import skew 

def emptyPicProfileFromURL(picProfileURL):

    """ Check if the URL of the Profile Pic contains the substring 
        "44884218_345707102882519_2446069589734326272_n.jpg" that is
        the name of the file that Instagram use for the emplty photo profile.
        The function returns true if the Profile Picture is not present, false otherwise.
    """

    emptyPicURL="44884218_345707102882519_2446069589734326272_n.jpg"

    return (emptyPicURL in picProfileURL)

#
# Dataset of real accounts
#

with open("RUdataset.json", 'r') as f:
    users = json.load(f)

data = []

for user in users:
    item = {}
    username = user["username"]
    # Profile picture present
    item["profile_pic"] = False if emptyPicProfileFromURL(user["profile_pic_url"]) else True
    # Biography present
    item["biography"] = False if user["biography"] == "" else True
    # Follows count
    item["follows_count"] = user["follows_count"]
    # Followed by count
    item["followed_by_count"] = user["followed_by_count"]
    # Follows count
    item["follows_count"] = user["follows_count"]
    # Follower/Followed ratio
    item["ff_ratio"] = item["followed_by_count"]/(item["follows_count"] + 1)
    # Media count
    item["media_count"] = user["media_count"]
    # Private
    item["is_private"] = user["is_private"]
    # Verified
    item["is_verified"] = user["is_verified"]
    # Is Business Account
    item["is_business_account"] = user["is_business_account"]
    # Is Joined recently
    item["is_joined_recently"] = user["is_joined_recently"]
    # Highlight reel count
    item["highlight_reel_count"] = user["highlight_reel_count"]
    # Connected Facebook Page
    item["connected_fb_page"] = False if user["connected_fb_page"] == None else True


    if os.path.isfile("C:/Users/ffran/OneDrive/Documenti/GitHub/instagram-profilechecker/users_posts/" + username + ".json"):
        with open("C:/Users/ffran/OneDrive/Documenti/GitHub/instagram-profilechecker/users_posts/" + username + ".json", encoding="utf8") as t:
            users_posts = json.load(t)
            comments = []
            likes = []
            dates = []
            videos = 0

            for post in users_posts["GraphImages"]:
                comments.append(post["edge_media_to_comment"]["count"])
                likes.append(post["edge_media_preview_like"]["count"])
                dates.append(post["taken_at_timestamp"])
                if post["is_video"]:
                    videos = videos + 1
            item["average_likes"] = statistics.mean(likes)
            item["max_likes"] = max(likes)
            item["min_likes"] = min(likes)            
            item["std_likes"] = None if len(likes) < 2 else statistics.stdev(likes)
            item["var_likes"] = None if len(likes) < 2 else statistics.variance(likes)
            item["skw_likes"] = skew(likes)

            item["average_comments"] = statistics.mean(comments)
            item["max_comments"] = max(comments)
            item["min_comments"] = min(comments) 
            item["std_comments"] = None if len(comments) < 2 else statistics.stdev(comments)
            item["var_comments"] = None if len(comments) < 2 else statistics.variance(comments)
            item["skw_comments"] = skew(comments)

            dates.reverse()
            times = [dates[i + 1] - dates[i] for i in range(len(dates)-1)]
            
            item["mean_time_between_posts"] = None if len(times) == 0 else statistics.mean(times)
            item["max_time_between_posts"] = None if len(times) == 0 else max(times)
            item["min_time_between_posts"] = None if len(times) == 0 else min(times) 
            item["std_time_between_posts"] = None if len(times) < 2 else statistics.stdev(times)
            item["var_time_between_posts"] = None if len(times) < 2 else statistics.variance(times)
            item["skw_time_between_posts"] = None if len(times) == 0 else skew(times)
    else:
        item["average_likes"] = None
        item["max_likes"] = None
        item["min_likes"] = None 
        item["std_likes"] = None
        item["var_likes"] = None
        item["skw_likes"] = None

        item["average_comments"] = None
        item["max_comments"] = None
        item["min_comments"] = None
        item["std_comments"] = None
        item["var_comments"] = None
        item["skw_comments"] = None

        item["mean_time_between_posts"] = None
        item["max_time_between_posts"] = None
        item["min_time_between_posts"] = None 
        item["std_time_between_posts"] = None
        item["var_time_between_posts"] = None
        item["skw_time_between_posts"] = None
    # Real account
    item["real_account"] = True
    data.append(item)
       


with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

    
    











