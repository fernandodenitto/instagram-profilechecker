import json
import os
import csv
import statistics
from scipy.stats import skew 
import pandas

with open('usernames/removed_list.txt', 'r') as f:
    myNames = [line.strip() for line in f]

print(myNames)


# data = []
# with open("data.json", 'r') as f:
#     users = json.load(f)

# for user in users:
#     item = {}
#     if user["media_count"] != 0 and user["average_likes"] is None:
#         item["username"]=user["username"]
#         item["media_count"]=user["media_count"]
#         item["average_likes"]=user["average_likes"]
#         item["is_private"]=user["is_private"]
#         item["real_account"]=user["real_account"]
#         data.append(item)
        



# df = pandas.DataFrame(data)
# df.to_csv("ErrorData.csv",index=False) 