#Script for take a list of username and create an array of JSON with the user fields for each user

# CONTEXT
import os
import sys
import json
from igramscraper.instagram import Instagram
from time import sleep
from random import randrange
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

proxies=[
    {
    'http': 'http://191.252.204.217:80',
    'https': 'https://191.252.204.217:80'
    },
    {
    'http': 'https://183.91.33.41:92',
    'https': 'https://183.91.33.41:92'
    }
]

# Lista di utenti daq usare per fare scraping
logins=[
     {   'username': 'querie_fornaini',
         'password':'Vietatofumare'
     },
    {   'username': 'nandobet92',
        'password':'datamining'
    },
    {   'username': 'nandocheck',
        'password':'datamining'
    },
    {   'username': 'mariorossi5775',
        'password':'vietatofumare'
    }
    
]

# Creo instanza di instagram
instagram=Instagram()

# Prendo un nuovo username dalla cima e lo inserisco in fondo alla lista logins
login_username=logins[0].get('username')
print("Loggato con: "+login_username)
login_password=logins[0].get('password')
logins = logins[1:] + logins[:1] 

# proxy=proxies[0]
# proxies = proxies[1:] + proxies[:1] 

# instagram.set_proxies(proxy)
instagram.with_credentials(login_username,login_password, 'pathtocache')
instagram.login()

# Open the file with the list of user we trust for sure (do a copy first because it will be modified!!!)
fru = open("real_users.txt", "r")
fruc = open("real_users_scraped.txt", "r")
frudataJson=open('RUdataset.json','r')


# Split all the user in the list in the file txt and remove \n as last character
usernameschecked=set(map(lambda text: text.replace('\n',''),fruc.readlines()))
fruc = open("real_users_scraped.txt", "a+")

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
        if indexSleep%20==0:
            # Prendo un nuovo username dalla cima e lo inserisco in fondo alla lista logins
            login_username=logins[0].get('username')
            login_password=logins[0].get('password')
            logins = logins[1:] + logins[:1] 
            # Imposto un nuovo proxy
            # proxy=proxies[0]
            # proxies = proxies[1:] + proxies[:1] 
            # instagram.set_proxies(proxy)

            sleep(randrange(60))
            instagram.with_credentials(login_username,login_password, 'pathtocache')
            instagram.login()
            print('Logged as: '+login_username)
        elif indexSleep%1000==0:
            sleep(100)
        else:
            sleep(10)
        account = instagram.get_account(username)
        userDatas.append(account.__dict__)
        # print(userDatas)
        fruc.write(username+'\n')
        print(str(indexSleep)+': '+username)
        indexSleep=indexSleep+1
    except:
        # If there are errors of any kind save the work and exit!
        userJson=json.dumps(userDatas)
        print('Ho gestito l eccezione!')
        # print(userJson)
        print(str(Exception))
        frudataJson.write(userJson)
        frudataJson.close()
        fruc.close()
        exit()

# If there are not errors save everything
userJson=json.dumps(userDatas)
frudataJson.write(userJson)
frudataJson.close()
fruc.close()
