class MFP():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        # url for website
        self.base_url = 'https://www.myfitnesspal.com'
        
        # login action
        self.login_action = '/account/login'
        
        # Firefox
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'
        }
    
    def login(self):
        