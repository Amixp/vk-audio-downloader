import vk

class User(object):

    def __init__(self):
        self.token = None
        self.user_id = None
        
    
    def authorise(self, app_id, scope):
        session = vk.InteractiveAuthSession(app_id='5071179', scope="audio") 
                          # Выводит запрос логина и пароля интерактивно
                          # в scope указываем к каким функциям нам необходим доступ
        self.token = session.access_token
         
        api = vk.API(session)
        info = api.audio.get() # пол 
        
        