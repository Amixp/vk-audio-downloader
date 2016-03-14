import vk

class MusicManager(object):
    '''
    classdocs
    '''


    def __init__(self, session):
        self.session = session
    
    def list_audio(self):  
        api = vk.API(self.session)          
        info = api.audio.get()
        
        audio_dict = {}
        for song in info:
            song_info = dict(song)
            audio_dict[song_info["url"]] = [song_info["title"],song_info["artist"]]
            
        return audio_dict
