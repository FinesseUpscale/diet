# standard library
from time import sleep
from random import uniform

# third party packages
import requests
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup

# custom modules
import mfp_helpers

class MFP():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        # url for website
        self.base_url = 'https://www.myfitnesspal.com'
        
        # login action
        self.login_url = 'https://www.myfitnesspal.com/account/login'
        
        # Firefox
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'
        }
        
        # establish persistent session across class
        self.session = requests.Session()
    
    def login(self):
        
        # grab the session
        s = self.session
        
        base = s.get(self.base_url)
        
        soup = BeautifulSoup(base.content, "html.parser")
        token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        self.headers.update({'authenticity_token': token})
        
        sleep(uniform(.55,1.4))
        
        login = s.post(self.login_url, headers=self.headers, auth=HTTPDigestAuth(self.username, self.password))
        soup = BeautifulSoup(login.content, "html.parser")
        print(soup)