import vk

class App(object):
    
    def __init__(self):
        self.app_id = '5071179'
        self.scope = "audio"
    
    def get_app_idd(self):
        return self.app_id
    
    def get_scope(self):
        return self.app_id
    
    def auth_user(self):
        login = input("Enter your login:\n")
        psw = input("Enter you password:\n")
        session = vk.AuthSession(self.app_id, login, psw, self.scope) 
        return session