from flask import Flask, jsonify, render_template, send_from_directory
from typing import Optional
import random
import json
import re
import requests

app = Flask(__name__)

# Load songs from songs.json
with open("./static/updated_songs.json", "r") as file:
    songs = json.load(file)

selected_songs = set()

def get_spotify_preview_url(spotify_track_id: str) -> Optional[str]:
    """
    Get the preview URL for a Spotify track using the embed page workaround.

    Args:
        spotify_track_id (str): The Spotify track ID

    Returns:
        Optional[str]: The preview URL if found, else None
    """
    try:
        embed_url = f"https://open.spotify.com/embed/track/{spotify_track_id}"
        response = requests.get(embed_url)
        response.raise_for_status()

        html = response.text
        match = re.search(r'"audioPreview":\s*{\s*"url":\s*"([^"]+)"', html)
        return match.group(1) if match else None

    except Exception as e:
        print(f"Failed to fetch Spotify preview URL: {e}")
        return None

@app.route('/api/spotify-preview/<track_id>', methods=['GET'])
def fetch_spotify_preview(track_id):
    preview_url = get_spotify_preview_url(track_id)
    if preview_url:
        return jsonify({'preview_url': preview_url})
    else:
        return jsonify({'error': 'Preview URL not found'}), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random_song", methods=["POST"])
def random_song():
    available_songs = [song for song in songs if song["title"] not in selected_songs]
    if not available_songs:
        return jsonify({"status": "error", "message": "Geen nummers meer beschikbaar!"})
    song = random.choice(available_songs)
    selected_songs.add(song["title"])
    return jsonify({"status": "success", "song": song, "available_songs": available_songs})

@app.route("/reset", methods=["POST"])
def reset_songs():
    selected_songs.clear()
    return jsonify({"status": "success", "message": "Alle nummers zijn gereset!"})

@app.route("/static/albums/<path:filename>")
def album_images(filename):
    return send_from_directory("static/albums", filename)

@app.route("/available_songs")
def available_songs():
    available_songs = [song for song in songs if song["title"] not in selected_songs]
    return jsonify(available_songs)

if __name__ == "__main__":
    app.run(debug=True)
