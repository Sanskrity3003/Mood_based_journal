import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Set your credentials (or use dotenv if preferred)
SPOTIPY_CLIENT_ID = "c24a832145ae41688f48dde8f4f5af22"
SPOTIPY_CLIENT_SECRET = "2e6c675f3fb643839add525e854f48ad"

client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def get_spotify_url(song_title, artist_name):
    query = f"track:{song_title} artist:{artist_name}"
    results = sp.search(q=query, type='track', limit=1)
    if results["tracks"]["items"]:
        return results["tracks"]["items"][0]["external_urls"]["spotify"]
    return None


def search_song(mood):
    results = sp.search(q=mood + " music", type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']
        return f"{name} - {artist}", url
    else:
        return "No track found", ""
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import re

# # Replace with your actual Spotify API credentials
# SPOTIFY_CLIENT_ID = "c24a832145ae41688f48dde8f4f5af22"
# SPOTIFY_CLIENT_SECRET = "2e6c675f3fb643839add525e854f48ad"

# # Set up the Spotify API client
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#     client_id=SPOTIFY_CLIENT_ID,
#     client_secret=SPOTIFY_CLIENT_SECRET
# ))

# def clean_song_name(song_name):
#     """
#     Extracts clean song title and artist from formatted string like:
#     "'Song Name' - Artist"
#     """
#     match = re.match(r"'(.*?)'\s*-\s*(.*)", song_name)
#     if match:
#         return match.group(1), match.group(2)
#     return song_name, ""  # fallback

# def get_spotify_track_url(song_name):
#     """
#     Searches Spotify for the given song and returns the track URL.
#     """
#     title, artist = clean_song_name(song_name)
#     query = f"{title} {artist}"
#     results = sp.search(q=query, type="track", limit=1)

#     if results["tracks"]["items"]:
#         track = results["tracks"]["items"][0]
#         return track["external_urls"]["spotify"]
#     else:
#         return None
