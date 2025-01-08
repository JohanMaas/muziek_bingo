from flask import Flask, jsonify, render_template, send_from_directory
import random

app = Flask(__name__)

# Mock song data
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
]
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
