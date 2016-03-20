import os
from urllib.request import urlopen

class SyncManager(object):

    def __init__(self):
        print(" ")

    def download(self, audio_info, name):
        url = audio_info
        file_name = name[1] + "-" + name[0]
        u = urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.get_all("Content-Length")[0])
        print("Downloading: {0} Bytes: {1}\n".format(file_name, file_size))

        track = u.read()
        f.write(track)

        # file_size_dl = 0
        # block_sz = 8192
        # while True:
        #     buffer = u.read(block_sz)
        #     if not buffer:
        #         break
        #
        #     file_size_dl += len(buffer)
        #     f.write(buffer)
        #     status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        #     status = status + chr(8)*(len(status)+1)
            # print(status)

        f.close()

    def download_audio(self, audio_info):
        os.mkdir("audio")
        os.chdir("audio")

        for song, name in audio_info.items():
            self.download(song, name)
