import json
import os
import csv
import pandas as pd
from shutil import copyfile


FtR = pd.read_csv("usernames/FakeToReal.csv", header=None)
FakeToReal = FtR[0].tolist()
RtF = pd.read_csv("usernames/RealToFake.csv", header=None)
RealToFake = RtF[0].tolist()

with open("users_data/RUdataset.json", 'r') as f:
    Rusers = json.load(f)

with open("users_data/FUdataset.json", 'r') as f:
    Fusers = json.load(f)

i=0
for user in Rusers:
    
    if user["username"] in RealToFake:
        Rusers.remove(user)
    
  
        
for user in Fusers:
    
    if user["username"] in FakeToReal:
        Rusers.append(user)
        Fusers.remove(user)

# for user in Rusers:
#     if os.path.isfile("users_posts/real_posts/"+ user["username"] + ".json"):
#         copyfile("users_posts/real_posts/"+ user["username"] + ".json", "modifiedData/users_posts/real_posts/"+ user["username"] + ".json")
#     if os.path.isfile("users_posts/fake_posts/"+ user["username"] + ".json"):
#         copyfile("users_posts/fake_posts/"+ user["username"] + ".json", "modifiedData/users_posts/real_posts/"+ user["username"] + ".json")

# for user in Fusers:
#     if os.path.isfile("users_posts/fake_posts/"+ user["username"] + ".json"):
#         copyfile("users_posts/fake_posts/"+ user["username"] + ".json", "modifiedData/users_posts/fake_posts/"+ user["username"] + ".json")
    
with open('modifiedData/RUdataset.json', 'w') as outfile:
    json.dump(Rusers, outfile, indent=4)

with open('modifiedData/FUdataset.json', 'w') as outfile:
    json.dump(Fusers, outfile, indent=4)


# copyfile("users_data/RUdataset.json", "modifiedData/RUdataset.json")







# print(x)
# if 'laansraf' in x:
#     print('yes')
# else:
#     print('no')
