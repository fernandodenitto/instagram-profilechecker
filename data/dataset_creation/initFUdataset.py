# CONTEXT
import os
import sys
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from igramscraper.instagram import Instagram

from time import sleep

instagram = Instagram()
instagram.with_credentials('nandobet92', 'datamining', 'pathtocache')
instagram.login()

sleep(2) # Delay to mimic user

# Open the file with the list of user we trust for sure
ftu = open("fake_users_origin.txt", "r")
# Split all the user in the list in the file txt and remove \n as last character
users=list(map(lambda text: text.replace('\n',''),ftu.readlines()))
print (users)

# Open the file where to collect the real instagram user toke from the following of the above trusted users
file=open('fake_users_ds.txt','a')

fakeUsersSet=set()

# For every username in the list take the first N followers and fill the real_users.txt file
for username in users:
    print(username)
    fakeUsersSet.add(username) #Add also the trusted fake
    sleep(10)
    account = instagram.get_account(username)
    sleep(2)

    #Set how many followers you want to obtain
    num_followers=100
    print(account.followed_by_count)
    
    # If the followers of the user are less take all the followers
    if (account.follows_count<num_followers):
        num_followers=account.followed_by_count


    followers = instagram.get_followers(account.identifier,num_followers,num_followers, delayed=True) 

    #For every user, append it in the list
    for follower in followers['accounts']:
        fakeUsersSet.add(follower.username)
        file.write(follower.username+'\n')
