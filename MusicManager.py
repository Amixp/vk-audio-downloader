import vk
import collections

class MusicManager(object):

    def __init__(self, session):
        self.session = session

    def show_audio(self, audio_dict):
        print(" ")
        count = 1
        for link, name in audio_dict.items():
            print("{0}) {1}-{2}".format(count, name[1], name[0]))
            count += 1


    def get_audio_list(self):
        api = vk.API(self.session)

        info = api.audio.get()

        audio_dict = collections.OrderedDict()
        for song in info:
            song_info = collections.OrderedDict(song)
            audio_dict[song_info["url"]] = [song_info["title"],song_info["artist"]]

        self.show_audio(audio_dict)

        audio_number = int(input("\nHow many tracks download?\n"))

        download_list = collections.OrderedDict()
        for i in range(audio_number):
            temp =  audio_dict.popitem(last=False)
            download_list[temp[0]] = temp[1]

        return download_list
