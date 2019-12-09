from context import Instagram # pylint: disable=no-name-in-module
from time import sleep
from JsonData import*
from parameters import*
import random 
import json
import io

class InstagramScraper:
    username = ''
    password = ''
   

    def __init__(self, usr, psw):
        self.username = usr
        self.password = psw

    def scrapeData(self, user):
        instagram = Instagram()
        
        instagram.with_credentials(username, password)
        instagram.login()

        starting_username = instagram.get_account(user)
        numberFollows = starting_username.follows_count
        following = instagram.get_following(starting_username.identifier, numberFollows, numberFollows, delayed=True)
        for following_user in following['accounts']:   
            sleep(1)
            account = instagram.get_account(following_user.username)
            sleep(1)
            medias = instagram.get_medias(following_user.username, following_user.media_count)
    
            data = createData(account)

            for media in medias:
                data = addMedia(data, media)
                with io.open('data/' + account.username + '.json', 'w', encoding='utf-8') as f:
                    f.write(json.dumps(data, ensure_ascii=False, indent=4))



