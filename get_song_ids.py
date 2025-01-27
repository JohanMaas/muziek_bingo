import requests, json

# Spotify API instellingen
CLIENT_ID = ""
CLIENT_SECRET = ""

# Songlijst
songs = [
...
]

# Token ophalen
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    return response.json()["access_token"]

# Track ID zoeken
def get_track_id(song, token):
    query = f"{song['title']} {song['artist']}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    results = response.json()
    if results["tracks"]["items"]:
        return results["tracks"]["items"][0]["id"]
    else:
        return None

# Main script
def main():
    token = get_access_token()
    updated_songs = []
    
    for song in songs:
        track_id = get_track_id(song, token)
        if track_id:
            song["track_id"] = track_id
            print(f"Track ID gevonden voor '{song['title']}': {track_id}")
        else:
            print(f"Geen track ID gevonden voor '{song['title']}'")
        updated_songs.append(song)

    # Resultaat printen of opslaan
    print(updated_songs)

    with open("updated_songs.json", "w") as file:
        json.dump(updated_songs, file, indent=4)

if __name__ == "__main__":
    main()
