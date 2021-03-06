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
        
        # account settings intermediate URL
        self.account_settings = 'https://www.myfitnesspal.com/account/settings'
        
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
        s.headers.update(self.headers)
        
        # visit the login url via GET so we can soup it for the access token
        base = s.get(self.login_url)
        
        # soup the response to the login URL GET request to scrape the token
        soup = BeautifulSoup(base.content, "html.parser")
        auth_token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        
        # add token to headers for continued authentication
        s.headers.update({'authenticity_token': auth_token})
        print(auth_token)
        
        # sleep for a moment before logging in
        sleep(uniform(1.4,3.1))
        
        # login to MFP
        login = s.post(self.login_url, headers=self.headers, verify=True,
            data={'username': self.username, 'password': self.password, 'remember_me':True})
        
        sleep(uniform(1.5,3))
        
        # access the account settings page
        account_settings = s.get(self.account_settings, headers=s.headers)
        new_token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        s.headers['authenticity_token'] = new_token
        print(new_token)
        
        sleep(uniform(1.4,3.1))
        
        # access the diary settings page
        diary = s.get(self.diary_url, verify=True, headers=s.headers)
        
        # soup the webpage with bs4
        soup = BeautifulSoup(diary.content, "html.parser")
        
        # grab the name of my first meal to see if this actually works
        # found the key 'mean_names[0][description]' via 'view page source' on browser
        meal0=soup.find('input', {'name': 'meal_names[0][description]'
            }).get('value')
        print(meal0)
        
        new_token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        s.headers['authenticity_token'] = new_token
        print(new_token)
        
        # do this https://brennan.io/2016/03/02/logging-in-with-requests/
        # See if there's a hidden CSRF token in the save changes form
        # if so, work around it
        
        # ~~~~~~~~ #
        #
        # cut off code for now
        #
        #
        # ~~~~~~~~ #
        
        # Great, we're in, now let's wait again so our request isn't ignored
        sleep(uniform(1.5,3))
        
        # Attempt to update the name of the first meal via POST method to
        # see if we can actually change it.
        
        diary_post=s.post(self.diary_url, headers=s.headers, verify=True,
            data={'username': self.username, 'password': self.password,
            'meal_names[0][description]': 'updated meal 0 test name'})
        
        print(diary_post.url)
        
        # this does not work, refreshing the webpage shows that
        # the mealnames are unchanged. However, the status code is 200.
        
        # Why is POST ineffective? Let's see what the response looks like
        # soup = BeautifulSoup(diary_post.content, "html.parser")
        # print(soup)
        
        # It prints the login page! Our session ended?
        # Why does this post method not work? It seems like I've done everything right.