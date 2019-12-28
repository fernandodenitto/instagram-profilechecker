import os
import sys
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from igramscraper.instagram import Instagram

from time import sleep

# instagram = Instagram()
# instagram.with_credentials('nandocheck', '', 'pathtocache')
# instagram.login()

# Open the file with the list of user we trust for sure
ftu = open("real_users.txt", "r")
# Split all the user in the list in the file txt and remove \n as last character
users=list(map(lambda text: text[:-1],ftu.readlines()))
#Remove the empty string (if there are!)
users=list(filter(None, users))
print (users)