#Script for take a list of username and create an array of JSON with the user fields for each user

# CONTEXT
import os
import sys
import json
from igramscraper.instagram import Instagram
from time import sleep
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


proxies={
    'https': 'https://201.217.4.101:53281',
}


instagram = Instagram()
instagram.set_proxies(proxies)
instagram.with_credentials('nandocheck','datamining', 'pathtocache')
instagram.login()



# sleep(2) # Delay to mimic user

# Open the file with the list of user we trust for sure (do a copy first because it will be modified!!!)
fru = open("real_users.txt", "r")
fruc = open("real_users_checked.txt", "r")
frudataJson=open('RUdataset.json','r')

# 
# Split all the user in the list in the file txt and remove \n as last character
usernameschecked=set(map(lambda text: text.replace('\n',''),fruc.readlines()))
fruc = open("real_users_checked.txt", "a+")

#Remove from the complete set of username the ones that we already checked
usernames=set(map(lambda text: text.replace('\n',''),fru.readlines()))-usernameschecked

print('Username scraped: '+str(len(usernameschecked)))
print('Username to scrape: '+str(len(usernames)))

userDatas=(json.loads(frudataJson.read()))
frudataJson=open('RUdataset.json','w+')
print('Username in JSON: '+str(len(userDatas)))

# Index for sleep sometimes
indexSleep=1

# For every username scrape the datas with some pause for simulate a user usage
for username in usernames:
    try:
        if indexSleep%30==0:
            sleep(35)
        elif(indexSleep%125==0):
            sleep(60)
        else:
            sleep(15)
        account = instagram.get_account(username)
        userDatas.append(account.__dict__)
        # print(userDatas)
        fruc.write(username+'\n')
        print(username)
        indexSleep=indexSleep+1
    except Exception:
        # If there are errors of any kind save the work and exit!
        userJson=json.dumps(userDatas)
        # print(userJson)
        print(str(Exception))
        frudataJson.write(userJson)
        frudataJson.close()
        fruc.close()
        exit()

# If there are not errors save everything
userJson=json.dumps(userDatas)
frudataJson.write(userJson)
fruc.close()