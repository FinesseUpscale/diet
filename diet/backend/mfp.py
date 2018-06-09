# standard library
from time import sleep
from random import uniform

# third party packages
import requests
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup

# custom modules
from mfp_helpers import *

class MFP():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        # url for website
        self.base_url = 'https://www.myfitnesspal.com'
        
        # login action
        self.login_url = 'https://www.myfitnesspal.com/account/login'
        
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
        login = s.post(self.login_url, headers=self.headers, verify=True, data={'username': self.username, 'password': self.password})
        
        # access the diary settings page
        # diary = s.get(self.diary_url, verify=True, headers=self.headers)
        # soup = BeautifulSoup(diary.content, "html.parser")
        # meal0=soup.find('input', {'name': 'meal_names[0][description]'}).get('value')
        # print(meal0)
        
        diary_post=s.post(self.diary_url, headers=self.headers, verify=True, data={'meal_names[0][description]': 'Appol :)'})
        print(diary_post.status_code)
        soup = BeautifulSoup(diary_post.content, "html.parser")
        meal0=soup.find('input', {'name': 'meal_names[0][description]'}).get('value')
        print(meal0)
        
        # payload = {'meal_names_0_description': 'Appol :)'}
        
        # diary_post = s.post(self.diary_url, headers=self.headers, data=payload)
        # soup = BeautifulSoup(diary_post.content, "html.parser")
        
        # print(soup)
        # meal0 = soup.find(id='meal_names_0_description')
        # print(meal0)
        
        # diary = s.post(self.diary_url, headers=self.headers, data=mealnames)
        