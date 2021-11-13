import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt
import json

open_config = open('config.json', 'r')
config = json.load(open_config)

my_id = config['my_id']
my_credential = config['my_credential']
ccm = SpotifyClientCredentials(client_id = my_id, client_secret= my_credential)
spotify = spotipy.Spotify(client_credentials_manager= ccm)

search_artist = input('Artist name : ')
num = int(input('How many songs? : '))
topSongs_Ids =[]
topSongsFeatures = []

def getIdByArtist(artist_name):
    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id

def getTopSongsIds(artist_name):
    #num = 10
    try:
        search_id = getIdByArtist(artist_name)
        artist_top_tracks = spotify.artist_top_tracks(search_id, country="JP")["tracks"]

        for i in range(num):
            topSongs_Ids.append(artist_top_tracks[i]['id'])
        return topSongs_Ids

    except IndexError:
        print("IndexError has occurred!")
    except AttributeError:
        print("AttributeError has occurred!")

def getTopSongsFeatures(artist_name):
    for ids in getTopSongsIds(artist_name):
        feature = spotify.audio_features(ids)
        topSongsFeatures.append(feature)
    return topSongsFeatures

def getTopSongsFeatureCerts(artist_name):
    y_list = []
    for feature in getTopSongsFeatures(artist_name):
        del feature[0]['key'], feature[0]['loudness'], feature[0]['tempo'], feature[0]['type'], feature[0]['id'], feature[0]['uri'], feature[0]['track_href'], feature[0]['analysis_url'], feature[0]['duration_ms'], feature[0]['time_signature']
        l = feature[0].items()
        x, y = zip(*l)
        y_list.append(y)
    ax = plt.subplot()
    for j in y_list:
        ax.plot(x,j)
    plt.grid()
    plt.title(f'{search_artist} : Top {num} Songs Features')
    plt.xticks(rotation=340)
    plt.show()

if __name__ == '__main__':
    getTopSongsFeatureCerts(search_artist)