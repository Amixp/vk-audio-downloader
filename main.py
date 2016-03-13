import vk
<<<<<<< HEAD

session = vk.InteractiveAuthSession(app_id='5071179', scope="audio") 
                          # Выводит запрос логина и пароля интерактивно
                          # в scope указываем к каким функциям нам необходим доступ
token = session.access_token 
api = vk.API(session)
info = api.audio.get() # пол
for song in info:
    try:
        print(song)
    except Exception: # у меня пару раз выдавало ошибку,
    				   # как я понял при попытке декодировать кириллицу
        print("Encoding error")
        

=======
>>>>>>> 88a936a39e68f3bae65e1d9eb3a9c0e3e2b41537
