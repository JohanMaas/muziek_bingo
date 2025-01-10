import requests, json

# Spotify API instellingen
CLIENT_ID = "ebc608df2381425a88e132224868a924"
CLIENT_SECRET = "baab42fd1eae4a018997893edb1ceb61"

# Songlijst
songs = [
    {"title": "Hey Jude", "artist": "The Beatles", "image": "hey_jude.jpg"},
    {"title": "(I Can't Get No) Satisfaction", "artist": "The Rolling Stones", "image": "satisfaction.jpg"},
    {"title": "Good Vibrations", "artist": "The Beach Boys", "image": "good_vibrations.jpg"},
    {"title": "Respect", "artist": "Aretha Franklin", "image": "respect.jpg"},
    {"title": "Suspicious Minds", "artist": "Elvis Presley", "image": "suspicious_minds.jpg"},
    {"title": "Mrs. Robinson", "artist": "Simon & Garfunkel", "image": "mrs_robinson.jpg"},
    {"title": "Stop! In the Name of Love", "artist": "The Supremes", "image": "stop_in_the_name_of_love.jpg"},
    {"title": "I'm a Believer", "artist": "The Monkees", "image": "im_a_believer.jpg"},
    {"title": "I Heard It Through the Grapevine", "artist": "Marvin Gaye", "image": "grapevine.jpg"},
    {"title": "These Boots Are Made for Walkin'", "artist": "Nancy Sinatra", "image": "boots.jpg"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "image": "bohemian.jpg"},
    {"title": "Dancing Queen", "artist": "ABBA", "image": "dancing_queen.jpg"},
    {"title": "Stayin' Alive", "artist": "Bee Gees", "image": "stayin_alive.jpg"},
    {"title": "Go Your Own Way", "artist": "Fleetwood Mac", "image": "go_your_own_way.jpg"},
    {"title": "Hotel California", "artist": "The Eagles", "image": "hotel_california.jpg"},
    {"title": "I Will Survive", "artist": "Gloria Gaynor", "image": "i_will_survive.jpg"},
    {"title": "Imagine", "artist": "John Lennon", "image": "imagine.jpg"},
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "image": "stairway_to_heaven.jpg"},
    {"title": "Heroes", "artist": "David Bowie", "image": "heroes.jpg"},
    {"title": "Hot Stuff", "artist": "Donna Summer", "image": "hot_stuff.jpg"},
    {"title": "Rivers of Babylon", "artist": "Boney M.", "image": "rivers_of_babylon.jpg"},
    {"title": "I Want You Back", "artist": "The Jackson 5", "image": "i_want_you_back.jpg"},
    {"title": "Your Song", "artist": "Elton John", "image": "your_song.jpg"},
    {"title": "Piano Man", "artist": "Billy Joel", "image": "piano_man.jpg"},
    {"title": "London Calling", "artist": "The Clash", "image": "london_calling.jpg"},
    {"title": "Billie Jean", "artist": "Michael Jackson", "image": "billie_jean.jpg"},
    {"title": "Like a Virgin", "artist": "Madonna", "image": "like_a_virgin.jpg"},
    {"title": "Livin' on a Prayer", "artist": "Bon Jovi", "image": "livin_on_a_prayer.jpg"},
    {"title": "Purple Rain", "artist": "Prince", "image": "purple_rain.jpg"},
    {"title": "With or Without You", "artist": "U2", "image": "with_or_without_you.jpg"},
    {"title": "Girls Just Want to Have Fun", "artist": "Cyndi Lauper", "image": "girls_just_want_to_have_fun.jpg"},
    {"title": "I Wanna Dance with Somebody", "artist": "Whitney Houston", "image": "wanna_dance.jpg"},
    {"title": "Careless Whisper", "artist": "George Michael", "image": "careless_whisper.jpg"},
    {"title": "Africa", "artist": "Toto", "image": "africa.jpg"},
    {"title": "Don't Stop Believin'", "artist": "Journey", "image": "dont_stop_believin.jpg"},
    {"title": "Every Breath You Take", "artist": "The Police", "image": "every_breath_you_take.jpg"},
    {"title": "Born in the U.S.A.", "artist": "Bruce Springsteen", "image": "born_in_the_usa.jpg"},
    {"title": "Sweet Dreams (Are Made of This)", "artist": "Eurythmics", "image": "sweet_dreams.jpg"},
    {"title": "Take On Me", "artist": "A-ha", "image": "take_on_me.jpg"},
    {"title": "Another One Bites the Dust", "artist": "Queen", "image": "another_one_bites_the_dust.jpg"},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "image": "smells_like_teen_spirit.jpg"},
    {"title": "...Baby One More Time", "artist": "Britney Spears", "image": "baby_one_more_time.jpg"},
    {"title": "I Want It That Way", "artist": "Backstreet Boys", "image": "i_want_it_that_way.jpg"},
    {"title": "I Will Always Love You", "artist": "Whitney Houston", "image": "i_will_always_love_you.jpg"},
    {"title": "My Heart Will Go On", "artist": "Celine Dion", "image": "my_heart_will_go_on.jpg"},
    {"title": "Wannabe", "artist": "Spice Girls", "image": "wannabe.jpg"},
    {"title": "Wonderwall", "artist": "Oasis", "image": "wonderwall.jpg"},
    {"title": "Losing My Religion", "artist": "R.E.M.", "image": "losing_my_religion.jpg"},
    {"title": "Man! I Feel Like a Woman!", "artist": "Shania Twain", "image": "man_i_feel_like_a_woman.jpg"},
    {"title": "Hero", "artist": "Mariah Carey", "image": "hero.jpg"},
    {"title": "Under the Bridge", "artist": "Red Hot Chili Peppers", "image": "under_the_bridge.jpg"},
    {"title": "No Scrubs", "artist": "TLC", "image": "no_scrubs.jpg"},
    {"title": "Ironic", "artist": "Alanis Morissette", "image": "ironic.jpg"},
    {"title": "Zombie", "artist": "The Cranberries", "image": "zombie.jpg"},
    {"title": "Truly Madly Deeply", "artist": "Savage Garden", "image": "truly_madly_deeply.jpg"},
    {"title": "Angels", "artist": "Robbie Williams", "image": "angels.jpg"},
    {"title": "No Limit", "artist": "2 Unlimited", "image": "no_limit.jpg"},
    {"title": "All That She Wants", "artist": "Ace of Base", "image": "all_that_she_wants.jpg"},
    {"title": "Song 2", "artist": "Blur", "image": "song_2.jpg"},
    {"title": "Gangsta's Paradise", "artist": "Coolio", "image": "gangstas_paradise.jpg"},
    {"title": "You Really Got Me", "artist": "The Kinks", "image": "you_really_got_me.jpg"},
    {"title": "September", "artist": "Earth, Wind & Fire", "image": "september.jpg"},
    {"title": "Hungry Like the Wolf", "artist": "Duran Duran", "image": "hungry_like_the_wolf.jpg"},
    {"title": "Sweet Child O' Mine", "artist": "Guns N' Roses", "image": "sweet_child_o_mine.jpg"},
    {"title": "Come As You Are", "artist": "Nirvana", "image": "come_as_you_are.jpg"},
    {"title": "Say My Name", "artist": "Destiny's Child", "image": "say_my_name.jpg"},
    {"title": "Beat It", "artist": "Michael Jackson", "image": "beat_it.jpg"},
    {"title": "Mamma Mia", "artist": "ABBA", "image": "mamma_mia.jpg"},
    {"title": "Let It Be", "artist": "The Beatles", "image": "let_it_be.jpg"},
    {"title": "Rocket Man", "artist": "Elton John", "image": "rocket_man.jpg"}
    # Voeg hier de rest van je nummers toe...
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
