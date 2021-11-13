import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import json

open_config = open('config.json', 'r')
config = json.load(open_config)

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
blue_print_playlist = 'https://open.spotify.com/playlist/7fB3JUi4K3BkuiLfzyqrH6?si=a585b79c7e524372'
My_generation_playlist = 'https://open.spotify.com/playlist/37i9dQZF1DX4OQAiraQRL0?si=d70a262225ea4a77'
running = 'https://open.spotify.com/playlist/3akv0d9Ih7tnUs8vWLOlIB?si=a3e48a5c0a8d4a31'
mahoyo_album = 'https://open.spotify.com/album/5BAI5mFLd5S9YdevUCnOrd?si=JGhKKpE7Ss67KMtvLf4Egw'

my_id = config['my_id']
my_credential = config['my_credential']
ccm = SpotifyClientCredentials(client_id = my_id, client_secret= my_credential)
spotify = spotipy.Spotify(client_credentials_manager= ccm)

results = spotify.album_tracks(mahoyo_album)
a = spotify.audio_features('1FiHwQuheDkhq9nNdNxOH9')

track_ids = [i['id'] for i in results['items']]

features = []
for j in track_ids:
    feature = spotify.audio_features(j)
    features.append(feature)

with open('features.json', 'w') as f:
    json.dump(a, f, indent=2)

#with open('test.json', 'w') as f:
#    json.dump(results, f, indent=2)