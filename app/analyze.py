import spotipy
from spotipy import Spotify
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


USERNAME = '121580312177' #your spotify username
CLIENT_ID = '4f93aa65a9904887809a00412e492438'#set at your developer account
CLIENT_SECRET = '0fbf0cd633ac4cb5a077becad8857539' #set at your developer account
REDIRECT_URI = 'http://google.com/' #set at your developer account, usually "http://localhost:8000"
#SCOPE = 'https://open.spotify.com/playlist/0fsnnUPGbp2kcgy6YrPrX2?si=2At6ZfqnRTmg4eMaRBO1uQ' # or else

# User ID: 12158032177

# Erase cache and prompt for user permission
token = util.prompt_for_user_token(username=USERNAME,
                                    # scope=SCOPE,
                                    client_id=CLIENT_ID,
                                    client_secret=CLIENT_SECRET,
                                    redirect_uri=REDIRECT_URI)
if token:
    sp = spotipy.Spotify(auth=token)
    # dig your api

client_credentials_manager = SpotifyClientCredentials(client_id='4f93aa65a9904887809a00412e492438', client_secret='0fbf0cd633ac4cb5a077becad8857539')

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

sp = spotipy.Spotify(auth=token)

def get_playlist_by_uri(playlist_uri):
    playlist_id = playlist_uri[17:]
    playlist_tracks = sp.playlist_tracks(playlist_id)





results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])





