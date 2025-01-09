from flask import Flask, jsonify, render_template, send_from_directory
import random
import json

app = Flask(__name__)

# Load songs from songs.json
with open("./static/songs.json", "r") as file:
    songs = json.load(file)

selected_songs = set()

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
