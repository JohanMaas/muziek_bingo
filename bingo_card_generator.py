from flask import Flask, render_template_string
import random

app = Flask(__name__)

# De songlist
songs = [
...
]

# Zorg dat er voldoende nummers zijn om unieke kaarten te maken
if len(songs) < 25:
    raise ValueError("De songlist moet minimaal 25 nummers bevatten om een bingo kaart te maken.")

# Aantal kaarten om te genereren
NUM_CARDS = 10

# Template voor de bingo kaart met afstreep functionaliteit
BINGO_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bingo Kaart {{ card_number }}</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
        table { margin: 0 auto; border-collapse: collapse; }
        td { width: 100px; height: 100px; border: 1px solid #000; text-align: center; vertical-align: middle; padding: 5px; position: relative; cursor: pointer; }
        td.checked::before { content: '✖'; font-size: 3em; color: black; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
        img { max-width: 90px; max-height: 90px; }
    </style>
</head>
<body>
    <h1>Bingo Kaart {{ card_number }}</h1>
    <table>
        {% for row in card %}
        <tr>
            {% for song in row %}
            <td onclick="toggleCheck(this)">
                <strong>{{ song.title }}</strong><br>
            </td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>

    <script>
        function toggleCheck(cell) {
            // Voeg of verwijder de 'checked' klasse om het kruis te tonen
            cell.classList.toggle("checked");
        }
    </script>
</body>
</html>
"""

# Functie om een unieke bingo kaart te genereren
def generate_bingo_card():
    selected_songs = random.sample(songs, 25)  # Kies willekeurig 25 nummers
    card = [selected_songs[i:i + 5] for i in range(0, 25, 5)]  # Zet ze in een 5x5 raster
    return card

# Genereer de kaarten vooraf
NUM_CARDS = 10
bingo_cards = [generate_bingo_card() for _ in range(NUM_CARDS)]

@app.route("/bingo_kaart_<int:card_number>")
def bingo_kaart(card_number):
    if 1 <= card_number <= NUM_CARDS:
        card = bingo_cards[card_number - 1]
        return render_template_string(BINGO_TEMPLATE, card_number=card_number, card=card)
    else:
        return "Kaart niet beschikbaar", 404

if __name__ == "__main__":
#    app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
