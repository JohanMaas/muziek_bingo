import os
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
spotify = Spotify(client_credentials_manager=client_credentials_manager)

# Define the song list
songs = [
...
]

# Create directories to store the images
os.makedirs("album_covers", exist_ok=True)

def download_image(url, save_path):
    """Download an image from a URL."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Iterate through the songs and fetch album covers
for song in songs:
    track_id = song.get("track_id")
    if not track_id:
        print(f"Skipping {song['title']} - No track ID provided.")
        continue

    try:
        # Fetch track details from Spotify
        track = spotify.track(track_id)
        album_name = track["album"]["name"]
        album_image_url = track["album"]["images"][0]["url"]  # High-res image URL
        save_path = f"album_covers/{song['image']}"

        # Download the album cover
        print(f"Fetching cover for {song['title']} from album: {album_name}")
        download_image(album_image_url, save_path)

    except Exception as e:
        print(f"Error fetching data for {song['title']}: {e}")
