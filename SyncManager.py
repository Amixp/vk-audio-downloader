import os
import sqlite3
from urllib.request import urlopen

class SyncManager(object):

    def __init__(self, audio_info):
        self.audio_info = audio_info

    def chache_in_db(self):
        conn = sqlite3.connect('audio_chache.sqlite')
        cur = conn.cursor()

        cur.executescript('''
        DROP TABLE IF EXISTS audio;

        CREATE TABLE audio(
        url TEXT NOT NULL PRIMARY KEY UNIQUE,
        artist TEXT,
        track TEXT);
        ''')


        for song, name in self.audio_info.items():
            cur.execute('''
            INSERT OR IGNORE INTO audio (url, artist, track)
            VALUES(?, ?, ?)''', (song, name[0], name[1]))

        conn.commit()

    def download(self, song, name):
        url = song
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

    def download_audio(self):
        if not os.path.isdirs('audio'):
            os.mkdir("audio")
        os.chdir("audio")

        for song, name in self.audio_info.items():
            self.download(song, name)
