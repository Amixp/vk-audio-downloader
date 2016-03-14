from App import  *
from MusicManager import MusicManager
from SyncManager import SyncManager

app = App()
session = app.auth_user()

manager = MusicManager(session)
songs = manager.list_audio()
sync = SyncManager

