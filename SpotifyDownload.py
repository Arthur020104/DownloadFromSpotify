import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from audio import DownloadAudio
import sys

def get_spotify_playlist_tracks(playlist_url, client_id, client_secret):
    # Authenticate with the Spotify API
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Extract playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1].split('?')[0]

    # Get the playlist data
    results = sp.playlist_tracks(playlist_id)
    #print(results)
    tracks = results['items']

    #print(results)

    # Continue fetching data if the playlist has more than 100 tracks
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    # Extract the names of the tracks
    song_names = []
    input_songs = []
    for track in tracks:
        input_songs.append( f"{track['track']['name']} {track['track']['artists'][0]['name']}" )
        song_names.append(track['track']['name'])
    remove_file(".cache")

    return song_names,input_songs

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been removed successfully.")
    except OSError as e:
        print(f"Error: {e}")


def DownloadFromPlaylist(path,PLAYLIST_URL):
 # Replace these with your actual credentials
    CLIENT_ID = '0678d61d43af480db57f5855d9feca0d'
    CLIENT_SECRET = 'key'
    songs, input_songs = get_spotify_playlist_tracks(PLAYLIST_URL, CLIENT_ID, CLIENT_SECRET)
    if songs:
        print("\n")
        for i in range(len(songs)):
            remove_last_line()
            print(f"{i}. Baixando {songs[i]}")
            try:
                DownloadAudio(input_songs[i],songs[i],1,path)
            except:
                continue
        remove_last_line()
        print("Finalizado")
        return 0, "Finalizado"
    else:
        return 1, "Nenhuma música encontrada nessa playlist."

def remove_last_line():
    sys.stdout.write('\033[F')  # Move cursor to the beginning of the previous line
    sys.stdout.write('\033[K')  # Clear the line
    sys.stdout.flush()


