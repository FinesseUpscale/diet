import requests

meals={
    0:'Leaf',
    1:'Crackor',
    2:'Stinky',
    3:'Grape',
    4:'Appol',
    5:'Bellay'
}

mealnames={
    'meal_names_0_description': meals[0],
    'meal_names_1_description': meals[1],
    'meal_names_2_description': meals[2],
    'meal_names_3_description': meals[3],
    'meal_names_4_description': meals[4],
    'meal_names_5_description': meals[5]
}



login_url="https://www.myfitnesspal.com/account/login"
diary_url='https://www.myfitnesspal.com/account/diary_settings'

with requests.Session() as s:
    
    # Prompt for login at commandline
    login_payload={
        'username': input("username: "),
        'password': input("password: "),
        'remember_me': True
    }
    
    login = s.post(login_url, data=login_payload)
    
    # https://stackoverflow.com/q/3463723/7709753
    # WWW-Authenticate header should contain methodology used
    # if(login.status_code!=200):
    test = s.get(diary_url)
    print(test.text)
    
    # go_to_diary = s.get(diary_url)
    # diary_page = s.post(diary_url, data=mealnames)