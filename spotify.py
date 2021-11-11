import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

album_url = 'https://open.spotify.com/album/30UlCONsAqm3hm5GiI1Wba?si=r-IWoyrPSAu_LdL8tLJAqQ'
artist_url = "https://open.spotify.com/artist/4vhezQRmmI48a5uigqV180?si=q-JgH0AqSRSHSw5195VJIg"
track_url = "https://open.spotify.com/playlist/37i9dQZEVXbKqiTGXuCOsB?si=0ba493c0aef24a01"
track_id = ''


my_id = '036b920c11d94e558431e6fb9d3aec09'
my_credential = 'f1308ce264c74028ad57965725faa161'
ccm = SpotifyClientCredentials(client_id = my_id, client_secret= my_credential)
sptify = spotipy.Spotify(client_credentials_manager= ccm)
results = sptify.album_tracks()

with open('test.json', 'w') as f:
    json.dump(results, f, indent=2)
