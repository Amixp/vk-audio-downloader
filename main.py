import vk

session = vk.InteractiveAuthSession(app_id='5071179', scope="audio") 
                          # Выводит запрос логина и пароля интерактивно
                          # в scope указываем к каким функциям нам необходим доступ
token = session.access_token 
api = vk.API(session)

# id = api.users.get_id() TODO: сделать получение id

info = api.audio.get()
  
for song in info:
    try:
        song_info = dict(song)
        artist = song_info["artist"]
        song = song_info["title"]
        url = song_info["url"]
    except Exception: # у меня пару раз выдавало ошибку,
    				   # как я понял при попытке декодировать кириллицу
        print("Encoding error")
<<<<<<< HEAD
=======
        

>>>>>>> 575001acbe06e2b38e224338bb16b1683226ae93
