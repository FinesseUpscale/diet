# standard library
from time import sleep
from random import uniform

# third party packages
import requests
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup

class MFP():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        # url for website
        self.base_url = 'https://www.myfitnesspal.com'
        
        # login action
        self.login_url = 'https://www.myfitnesspal.com/account/login'
        
        # page that contains diary information we want to update
        self.diary_url = 'https://www.myfitnesspal.com/account/diary_settings'
        
        # Firefox
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'
        }
        
        # establish persistent session across class
        self.session = requests.Session()
    
    def login(self):
        
        # grab the session
        s = self.session
        
        base = s.get(self.login_url)
        
        soup = BeautifulSoup(base.content, "html.parser")
        token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        self.headers.update({'authenticity_token': token})
        
        sleep(uniform(.55,1.4))
        
        # login to MFP
        login = s.post(self.login_url, headers=self.headers, verify=True,
            data={'username': self.username, 'password': self.password})
        
        # access the diary settings page
        diary = s.get(self.diary_url, verify=True, headers=self.headers)
        
        # parse the webpage with bs4
        soup = BeautifulSoup(diary.content, "html.parser")
        
        # grab the name of my first meal to see if this actually works
        meal0=soup.find('input', {'name': 'meal_names[0][description]'
            }).get('value')
        # print meal to visually check it's right (it is)
        print(meal0)
        
        # Great, we're in, now let's wait a sec just so we seem normal
        sleep(uniform(.55,1.4))
        
        # Attempt to update the name of the first meal via POST method to
        # see if we can actually change it. (It doesn't, mealname is unchanged).
        diary_post=s.post(self.diary_url, headers=self.headers, verify=True,
            data={'meal_names[0][description]': 'updated meal 0 test name'})
        
        # Above code doesn't work. Status code is 200, so that's not the issue
        # so check to see what the diary_post response actually looks like
        soup = BeautifulSoup(diary_post.content, "html.parser")
        print(soup)
        # It prints the login page! Our session ended!
        # Why does this post method not work? It seems like I've done everything right.