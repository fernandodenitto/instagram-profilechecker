# CONTEXT
import os
import sys
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from igramscraper.instagram import Instagram

from time import sleep

instagram = Instagram()
instagram.with_credentials('nandocheck', '', 'pathtocache')
instagram.login()

sleep(2) # Delay to mimic user

# Open the file with the list of user we trust for sure
ftu = open("trusted_user.txt", "r")
# Split all the user in the list in the file txt and remove \n as last character
users=list(map(lambda text: text[:-1],ftu.readlines()))
#Remove the empty string (if there are!)
users=list(filter(None, users))
print (users)

# Open the file where to collect the real instagram user toke from the following of the above trusted users
file=open('real_users.txt','a')


# For every username in the list take the first 500 followings and fill the real_users.txt file
for username in users:
    sleep(10)
    account = instagram.get_account(username)
    sleep(2)

    #Set how many followings you want to obtain
    num_following=500
    
    # If the following of the user are less take all the followings
    if (account.follows_count<=num_following):
        num_following=account.follows_count

    following = instagram.get_following(account.identifier,num_following,100, delayed=True) 

    #For every user, append it in the list
    for following_user in following['accounts']:
        #Print the username lists in a file
        file.write(following_user.username+'\n')
        print(following_user.username+'\n')



# # Convert the array of dictionaries in JSON and store in a file call with the name of the user we use to scrape
# with open(username+'_following1000.json', 'w') as outfile:
#     json.dump(userList, outfile)

# LO SCOPO È CREARE UN LISTONE DI DI USERNAME DI UTENTI REALI E DOPO CREARE UNO SCRIPT CHE PRENDE I DATI AD UNO AD UNO
# CON UN DELAY CHE POSSA NON DARE FASTIDIO A NESSUNO