from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

mood_songs = {
    "Happy": [
        {"Mood": "Happy", "Quote": "Happiness is a journey, not a destination.", "Song": "Love You Zindagi - Dear Zindagi", "link": "https://youtu.be/bw7bVpI5VcM"},
        {"Mood": "Happy", "Quote": "Smile, it’s free therapy.", "Song": "Phir Se Ud Chala - Rockstar", "link": "https://youtu.be/-3gQ6HIkRys"},
        {"Mood": "Happy", "Quote": "One whose happiness is within … attains liberation.", "Song": "Dil Dhadkane Do - ZNMD", "link": "https://youtu.be/PyTaSNvflM0"}
    ],
    "Sad": [
        {"Mood": "Sad", "Quote": "Tears are words that the heart can’t express.", "Song": "Agar Tum Saath Ho - Tamasha", "link": "https://youtu.be/dhY8jRNELUc"},
        {"Mood": "Sad", "Quote": "Sometimes you just need a good cry.", "Song": "Ae Dil Hai Mushkil", "link": "https://youtu.be/6FURuLYrR_Q"},
        {"Mood": "Sad", "Quote": "Every storm runs out of rain.", "Song": "Raabta - Agent Vinod", "link": "https://youtu.be/zAU_rsoS5ok"}
    ],
    "Emotional": [
        {"Mood": "Emotional", "Quote": "Sometimes the heaviest burdens are the ones we carry silently.", "Song": "Kun Faya Kun - Rockstar", "link": "https://youtu.be/0RDI9CMilhk"}
    ],
    "Neutral": [
        {"Mood": "Neutral", "Quote": "Every day is a page in your life story.", "Song": "Shaam - Aisha", "link": "https://youtu.be/8WGBtD1v5tM"}
    ],
    "Angry": [
        {"Mood": "Angry", "Quote": "Anger is one letter short of danger.", "Song": "Bulleya - ADHM", "link": "https://youtu.be/FJ55SHCzt88"}
    ],
    "Love": [
        {"Mood": "Love", "Quote": "You are my today and all of my tomorrows.", "Song": "Tum Mile", "link": "https://youtu.be/WJAEZpTn5yQ"}
    ],
    "Excited": [
        {"Mood": "Excited", "Quote": "Adventure begins the moment you feel alive.", "Song": "Ilahi - YJHD", "link": "https://youtu.be/sKVqH0MYlXY"}
    ],
    "Relaxed": [
        {"Mood": "Relaxed", "Quote": "Breathe deeply; even the quietest moments have their melody.", "Song": "Kabira - YJHD", "link": "https://youtu.be/jHNNMj5bNQw"}
    ],
    "Romantic": [
        {"Mood": "Romantic", "Quote": "Love makes life magical.", "Song": "Janam Janam - Dilwale", "link": "https://youtu.be/gvyUuxdRdR4"}
    ]
}


@app.route('/')
def index():
    return render_template("index.html", username="User")  # Replace with dynamic login later

@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/mood/<mood>')
def mood_page(mood):
    mood = mood.capitalize()
    if mood not in mood_songs:
        return "Mood not found!", 404
    choice = random.choice(mood_songs[mood])
    return render_template("mood.html", mood=choice["Mood"], quote=choice["Quote"], song=choice["Song"], link=choice["link"])


@app.route('/play/<mood>')
def play_song(mood):
    if mood not in mood_songs:
        return "Mood not found!", 404
    choice = random.choice(mood_songs[mood])
    return redirect(choice["link"])


if __name__ == "__main__":
    app.run(debug=True)
