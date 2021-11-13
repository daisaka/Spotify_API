import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.client import Spotify
import json

open_config = open('config.json', 'r')
config = json.load(open_config)

my_id = config['my_id']
my_credential = config['my_credential']
ccm = SpotifyClientCredentials(client_id = my_id, client_secret= my_credential)
spotify = spotipy.Spotify(client_credentials_manager= ccm)

search_artist = input('input artist name:')

def getIdByArtist(artist_name):
    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id

def getTopSongs(artist_name):
    num = 10
    try:
        search_id = getIdByArtist(artist_name)
        artist_top_tracks = spotify.artist_top_tracks(search_id, country="JP")["tracks"]

        print(artist_name + f" Top{num} Songs")

        for i in range(num):
            print(str(i + 1) + ". " + artist_top_tracks[i]["name"])

    except IndexError:
        print("IndexError has occurred!")
    except AttributeError:
        print("AttributeError has occurred!")

if __name__ == '__main__':
    getTopSongs(search_artist)
