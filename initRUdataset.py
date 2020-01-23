# CONTEXT
import os
import sys
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from igramscraper.instagram import Instagram

from time import sleep

instagram = Instagram()
instagram.with_credentials('nandocheck', 'datamining', 'pathtocache')
instagram.login()

sleep(2) # Delay to mimic user

# Open the file with the list of user we trust for sure
ftu = open("real_users_origin.txt", "r")
# Split all the user in the list in the file txt and remove \n as last character
users=list(map(lambda text: text.replace('\n',''),ftu.readlines()))
print (users)

# Open the file where to collect the real instagram user toke from the following of the above trusted users
file=open('real_users.txt','a')

realUserSet=set()

# For every username in the list take the first 500 followings and fill the real_users.txt file
for username in users:
    print(username)
    sleep(10)
    account = instagram.get_account(username)
    sleep(2)

    #Set how many followings you want to obtain
    num_following=600
    
    # If the following of the user are less take all the followings
    if (account.follows_count<num_following):
        num_following=account.follows_count


    following = instagram.get_following(account.identifier,num_following,100, delayed=True) 

    #For every user, append it in the list
    for following_user in following['accounts']:
        realUserSet.add(following_user.username)
        file.write(following_user.username+'\n')
