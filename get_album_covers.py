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
   {
        "title": "Hey Jude",
        "artist": "The Beatles",
        "image": "hey_jude.jpg",
        "track_id": "1eT2CjXwFXNx6oY5ydvzKU"
    },
    {
        "title": "(I Can't Get No) Satisfaction",
        "artist": "The Rolling Stones",
        "image": "satisfaction.jpg",
        "track_id": "2PzU4IB8Dr6mxV3lHuaG34"
    },
    {
        "title": "Good Vibrations",
        "artist": "The Beach Boys",
        "image": "good_vibrations.jpg",
        "track_id": "6aU6a9tdn2vHhnPGlboFZX"
    },
    {
        "title": "Respect",
        "artist": "Aretha Franklin",
        "image": "respect.jpg",
        "track_id": "7s25THrKz86DM225dOYwnr"
    },
    {
        "title": "Suspicious Minds",
        "artist": "Elvis Presley",
        "image": "suspicious_minds.jpg",
        "track_id": "1H5IfYyIIAlgDX8zguUzns"
    },
    {
        "title": "Mrs. Robinson",
        "artist": "Simon & Garfunkel",
        "image": "mrs_robinson.jpg",
        "track_id": "0iOZM63lendWRTTeKhZBSC"
    },
    {
        "title": "Stop! In the Name of Love",
        "artist": "The Supremes",
        "image": "stop_in_the_name_of_love.jpg",
        "track_id": "52FlwUMMDnTK8TGkCag9Jd"
    },
    {
        "title": "I'm a Believer",
        "artist": "The Monkees",
        "image": "im_a_believer.jpg",
        "track_id": "1CSLeVCXmetBh8IkTPMFdL"
    },
    {
        "title": "I Heard It Through the Grapevine",
        "artist": "Marvin Gaye",
        "image": "grapevine.jpg",
        "track_id": "1tqT6DhmsrtQgyCKUwotiw"
    },
    {
        "title": "These Boots Are Made for Walkin'",
        "artist": "Nancy Sinatra",
        "image": "boots.jpg",
        "track_id": "2PneNdtypG6XcgmWmGd9FI"
    },
    {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "image": "bohemian.jpg",
        "track_id": "3z8h0TU7ReDPLIbEnYhWZb"
    },
    {
        "title": "Dancing Queen",
        "artist": "ABBA",
        "image": "dancing_queen.jpg",
        "track_id": "0GjEhVFGZW8afUYGChu3Rr"
    },
    {
        "title": "Stayin' Alive",
        "artist": "Bee Gees",
        "image": "stayin_alive.jpg",
        "track_id": "5ubvP9oKmxLUVq506fgLhk"
    },
    {
        "title": "Go Your Own Way",
        "artist": "Fleetwood Mac",
        "image": "go_your_own_way.jpg",
        "track_id": "15rjQH7nTcTomKwfVMd4xl"
    },
    {
        "title": "Hotel California",
        "artist": "The Eagles",
        "image": "hotel_california.jpg",
        "track_id": "40riOy7x9W7GXjyGp4pjAv"
    },
    {
        "title": "I Will Survive",
        "artist": "Gloria Gaynor",
        "image": "i_will_survive.jpg",
        "track_id": "7rIovIsXE6kMn629b7kDig"
    },
    {
        "title": "Imagine",
        "artist": "John Lennon",
        "image": "imagine.jpg",
        "track_id": "7pKfPomDEeI4TPT6EOYjn9"
    },
    {
        "title": "Stairway to Heaven",
        "artist": "Led Zeppelin",
        "image": "stairway_to_heaven.jpg",
        "track_id": "5CQ30WqJwcep0pYcV4AMNc"
    },
    {
        "title": "Heroes",
        "artist": "David Bowie",
        "image": "heroes.jpg",
        "track_id": "7Jh1bpe76CNTCgdgAdBw4Z"
    },
    {
        "title": "Hot Stuff",
        "artist": "Donna Summer",
        "image": "hot_stuff.jpg",
        "track_id": "2zMJN9JvDlvGP4jB03l1Bz"
    },
    {
        "title": "Rivers of Babylon",
        "artist": "Boney M.",
        "image": "rivers_of_babylon.jpg",
        "track_id": "78His8pbKjbDQF7aX5asgv"
    },
    {
        "title": "I Want You Back",
        "artist": "The Jackson 5",
        "image": "i_want_you_back.jpg",
        "track_id": "5LxvwujISqiB8vpRYv887S"
    },
    {
        "title": "Your Song",
        "artist": "Elton John",
        "image": "your_song.jpg",
        "track_id": "38zsOOcu31XbbYj9BIPUF1"
    },
    {
        "title": "Piano Man",
        "artist": "Billy Joel",
        "image": "piano_man.jpg",
        "track_id": "70C4NyhjD5OZUMzvWZ3njJ"
    },
    {
        "title": "London Calling",
        "artist": "The Clash",
        "image": "london_calling.jpg",
        "track_id": "124Y9LPRCAz3q2OP0iCvcJ"
    },
    {
        "title": "Billie Jean",
        "artist": "Michael Jackson",
        "image": "billie_jean.jpg",
        "track_id": "5ChkMS8OtdzJeqyybCc9R5"
    },
    {
        "title": "Like a Virgin",
        "artist": "Madonna",
        "image": "like_a_virgin.jpg",
        "track_id": "1ZPlNanZsJSPK5h9YZZFbZ"
    },
    {
        "title": "Livin' on a Prayer",
        "artist": "Bon Jovi",
        "image": "livin_on_a_prayer.jpg",
        "track_id": "37ZJ0p5Jm13JPevGcx4SkF"
    },
    {
        "title": "Purple Rain",
        "artist": "Prince",
        "image": "purple_rain.jpg",
        "track_id": "1uvyZBs4IZYRebHIB1747m"
    },
    {
        "title": "With or Without You",
        "artist": "U2",
        "image": "with_or_without_you.jpg",
        "track_id": "4N0fzRX3T7QkOecp3pkWpp"
    },
    {
        "title": "Girls Just Want to Have Fun",
        "artist": "Cyndi Lauper",
        "image": "girls_just_want_to_have_fun.jpg",
        "track_id": "4y1LsJpmMti1PfRQV9AWWe"
    },
    {
        "title": "I Wanna Dance with Somebody",
        "artist": "Whitney Houston",
        "image": "wanna_dance.jpg",
        "track_id": "2tUBqZG2AbRi7Q0BIrVrEj"
    },
    {
        "title": "Careless Whisper",
        "artist": "George Michael",
        "image": "careless_whisper.jpg",
        "track_id": "5WDLRQ3VCdVrKw0njWe5E5"
    },
    {
        "title": "Africa",
        "artist": "Toto",
        "image": "africa.jpg",
        "track_id": "2374M0fQpWi3dLnB54qaLX"
    },
    {
        "title": "Don't Stop Believin'",
        "artist": "Journey",
        "image": "dont_stop_believin.jpg",
        "track_id": "77NNZQSqzLNqh2A9JhLRkg"
    },
    {
        "title": "Every Breath You Take",
        "artist": "The Police",
        "image": "every_breath_you_take.jpg",
        "track_id": "1JSTJqkT5qHq8MDJnJbRE1"
    },
    {
        "title": "Born in the U.S.A.",
        "artist": "Bruce Springsteen",
        "image": "born_in_the_usa.jpg",
        "track_id": "7FwBtcecmlpc1sLySPXeGE"
    },
    {
        "title": "Sweet Dreams (Are Made of This)",
        "artist": "Eurythmics",
        "image": "sweet_dreams.jpg",
        "track_id": "1TfqLAPs4K3s2rJMoCokcS"
    },
    {
        "title": "Take On Me",
        "artist": "A-ha",
        "image": "take_on_me.jpg",
        "track_id": "2WfaOiMkCvy7F5fcp2zZ8L"
    },
    {
        "title": "Another One Bites the Dust",
        "artist": "Queen",
        "image": "another_one_bites_the_dust.jpg",
        "track_id": "2k1yPYf9WGA4LiqcLVwtzn"
    },
    {
        "title": "Smells Like Teen Spirit",
        "artist": "Nirvana",
        "image": "smells_like_teen_spirit.jpg",
        "track_id": "4CeeEOM32jQcH3eN9Q2dGj"
    },
    {
        "title": "...Baby One More Time",
        "artist": "Britney Spears",
        "image": "baby_one_more_time.jpg",
        "track_id": "3MjUtNVVq3C8Fn0MP3zhXa"
    },
    {
        "title": "I Want It That Way",
        "artist": "Backstreet Boys",
        "image": "i_want_it_that_way.jpg",
        "track_id": "47BBI51FKFwOMlIiX6m8ya"
    },
    {
        "title": "I Will Always Love You",
        "artist": "Whitney Houston",
        "image": "i_will_always_love_you.jpg",
        "track_id": "4eHbdreAnSOrDDsFfc4Fpm"
    },
    {
        "title": "My Heart Will Go On",
        "artist": "Celine Dion",
        "image": "my_heart_will_go_on.jpg",
        "track_id": "33LC84JgLvK2KuW43MfaNq"
    },
    {
        "title": "Wannabe",
        "artist": "Spice Girls",
        "image": "wannabe.jpg",
        "track_id": "1Je1IMUlBXcx1Fz0WE7oPT"
    },
    {
        "title": "Wonderwall",
        "artist": "Oasis",
        "image": "wonderwall.jpg",
        "track_id": "1qPbGZqppFwLwcBC1JQ6Vr"
    },
    {
        "title": "Losing My Religion",
        "artist": "R.E.M.",
        "image": "losing_my_religion.jpg",
        "track_id": "31AOj9sFz2gM0O3hMARRBx"
    },
    {
        "title": "Man! I Feel Like a Woman!",
        "artist": "Shania Twain",
        "image": "man_i_feel_like_a_woman.jpg",
        "track_id": "2mqaYmF0XmV8egZB6jQOtN"
    },
    {
        "title": "Hero",
        "artist": "Mariah Carey",
        "image": "hero.jpg",
        "track_id": "5mgCMlxQW7fmHbrdJuowbB"
    },
    {
        "title": "Under the Bridge",
        "artist": "Red Hot Chili Peppers",
        "image": "under_the_bridge.jpg",
        "track_id": "3d9DChrdc6BOeFsbrZ3Is0"
    },
    {
        "title": "No Scrubs",
        "artist": "TLC",
        "image": "no_scrubs.jpg",
        "track_id": "1KGi9sZVMeszgZOWivFpxs"
    },
    {
        "title": "Ironic",
        "artist": "Alanis Morissette",
        "image": "ironic.jpg",
        "track_id": "29YBihzQOmat0U74k4ukdx"
    },
    {
        "title": "Zombie",
        "artist": "The Cranberries",
        "image": "zombie.jpg",
        "track_id": "7EZC6E7UjZe63f1jRmkWxt"
    },
    {
        "title": "Truly Madly Deeply",
        "artist": "Savage Garden",
        "image": "truly_madly_deeply.jpg",
        "track_id": "013AWvizllIUEC2FOBzOnh"
    },
    {
        "title": "Angels",
        "artist": "Robbie Williams",
        "image": "angels.jpg",
        "track_id": "1M2nd8jNUkkwrc1dgBPTJz"
    },
    {
        "title": "No Limit",
        "artist": "2 Unlimited",
        "image": "no_limit.jpg",
        "track_id": "1hGvGM76KOX6tpAyaHB0au"
    },
    {
        "title": "All That She Wants",
        "artist": "Ace of Base",
        "image": "all_that_she_wants.jpg",
        "track_id": "6kWJvPfC4DgUpRsXKNa9z9"
    },
    {
        "title": "Song 2",
        "artist": "Blur",
        "image": "song_2.jpg",
        "track_id": "3GfOAdcoc3X5GPiiXmpBjK"
    },
    {
        "title": "Gangsta's Paradise",
        "artist": "Coolio",
        "image": "gangstas_paradise.jpg",
        "track_id": "1DIXPcTDzTj8ZMHt3PDt8p"
    },
    {
        "title": "You Really Got Me",
        "artist": "The Kinks",
        "image": "you_really_got_me.jpg",
        "track_id": "6tZdL3Zp8JgrfDbsSeSV1S"
    },
    {
        "title": "September",
        "artist": "Earth, Wind & Fire",
        "image": "september.jpg",
        "track_id": "3kXoKlD84c6OmIcOLfrfEs"
    },
    {
        "title": "Hungry Like the Wolf",
        "artist": "Duran Duran",
        "image": "hungry_like_the_wolf.jpg",
        "track_id": "2qeESyQyH7MRHCBotCQsNq"
    },
    {
        "title": "Sweet Child O' Mine",
        "artist": "Guns N' Roses",
        "image": "sweet_child_o_mine.jpg",
        "track_id": "7snQQk1zcKl8gZ92AnueZW"
    },
    {
        "title": "Come As You Are",
        "artist": "Nirvana",
        "image": "come_as_you_are.jpg",
        "track_id": "2RsAajgo0g7bMCHxwH3Sk0"
    },
    {
        "title": "Say My Name",
        "artist": "Destiny's Child",
        "image": "say_my_name.jpg",
        "track_id": "7H6ev70Weq6DdpZyyTmUXk"
    },
    {
        "title": "Beat It",
        "artist": "Michael Jackson",
        "image": "beat_it.jpg",
        "track_id": "1OOtq8tRnDM8kG2gqUPjAj"
    },
    {
        "title": "Mamma Mia",
        "artist": "ABBA",
        "image": "mamma_mia.jpg",
        "track_id": "2TxCwUlqaOH3TIyJqGgR91"
    },
    {
        "title": "Let It Be",
        "artist": "The Beatles",
        "image": "let_it_be.jpg",
        "track_id": "7iN1s7xHE4ifF5povM6A48"
    },
    {
        "title": "Rocket Man",
        "artist": "Elton John",
        "image": "rocket_man.jpg",
        "track_id": "3gdewACMIVMEWVbyb8O9sY"
    }
    # Add more songs as needed
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
