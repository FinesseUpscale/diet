import requests
from bs4 import BeautifulSoup

import diet_helpers



base_url='https://www.myfitnesspal.com'
login_url="https://www.myfitnesspal.com/account/login"
diary_url='https://www.myfitnesspal.com/account/diary_settings'

with requests.Session() as s:
    
    base = s.get(base_url)
    
    soup = BeautifulSoup(base.content, "html.parser")
    token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
    print(token)
    
    # # Prompt for login at commandline
    # login_payload={
    #     'username': input("username: "),
    #     'password': input("password: "),
    #     'remember_me': True
    # }
    
    login_pyld = get_login()
    
    # header_payload = {
        
    # }
    
    # login = s.post(login_url, data=login_payload, headers={})
    
    # soup = BeautifulSoup(login)
    
    # # https://stackoverflow.com/q/3463723/7709753
    # # WWW-Authenticate header should contain methodology used
    # # if(login.status_code!=200):
    # test = s.get(diary_url)
    # print(test.text)
    
    # # go_to_diary = s.get(diary_url)
    # # diary_page = s.post(diary_url, data=mealnames)
    # #elf.opener.addheaders[('User-agent', 'Mozilla/5.0')]
    # #https://stackoverflow.com/questions/13825278/python-request-with-authentication-access-token
    
def get_login():
    
    # ask for username
    username = input("username: ")
    # ask for password
    password = input("password: ")
    
    # package username and password in a dictionary
    out = {
        'username': username,
        'password': password
    }
    
    # return the dictionary
    return out