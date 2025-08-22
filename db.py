import pandas as pd
import os
import random
from tabulate import tabulate 

# Folder for storing csv files
folder_name = "mood_data"
os.makedirs(folder_name, exist_ok=True)

# Mood data dictionary
mood_data = {
    
    "Happy": [
        {"Mood": "Happy", "Quote": "Happiness is a journey, not a destination.", "Song": "love you zindagi - dear zindagi", "link": "https://youtu.be/bw7bVpI5VcM?si=xW9jR7TNb4e9GwvR"},
        {"Mood": "Happy", "Quote": "Smile, it’s free therapy.", "Song": "phir se udd chala - Rockstar", "link": "https://youtu.be/-3gQ6HIkRys?si=wrUlnIxo_QMuOtiU"},
        {"Mood": "Happy", "quote" : "One whose happiness is within … attains liberation.","Song":"Dil Dhadkane do - Zindagi na milegi dobara","link":"https://youtu.be/PyTaSNvflM0?si=BDvdssDCiwc5s4Cu"},
        {"Mood": "Happy", "Quote": "Detached from external contacts, he finds happiness in the Self.","song":"Man ki Lagan - Paap","link" :"https://youtu.be/tuxzfwUVSlE?si=Y_uThfWSsL5qvJUx"},
        {"Mood": "Happy", "Quote": "A day without laughter is a day wasted.", "Song": "Gallan goodiyan - dil dhadkane do", "link": "https://youtu.be/jCEdTq3j-0U?si=b1u1heCu7cUMGrC2"}
    ],
    "Sad": [
        {"Mood": "Sad",  "Quote": "Tears are words that the heart can’t express.", "Song": "Agar tum saath ho - Tamasha","link":"https://youtu.be/dhY8jRNELUc?si=qnAUN2uC7A6IhB6d"},
        {"Mood": "Sad",  "Quote": "Sometimes you just need a good cry.", "Song": "Ae dil hai mushkil - Ae dil hai mushkil","link":"https://youtu.be/6FURuLYrR_Q?si=mj46gzBAmj5Qomth" },
        {"Mood" : "Sad", "Quote": "Every storm runs out of rain.", "Song": "Raabta - agent vinod","link":"https://youtu.be/zAU_rsoS5ok?si=Dzh6ROOBNqdWKqOU" },
        {"Mood": "Sad",  "Quote":"For one who is born, death is certain… therefore you should not lament","song":"Zinda - lootera","link":"https://youtu.be/cgHLvt0rxmM?si=zBg79n47rWq9Vwxw"},
        {"Mood": "Sad",  "quote": "You grieve for what is not worthy of grief; the wise lament neither for the living nor the dead.","song":"Chale chalo - Lagan","link":"https://youtu.be/LQmHKl3oNu0?si=VVULvroUZ45Lr6Gt" }
    ],
    "Emotional": [
        {"Mood": "Emotional", "Quote": "Wherever the restless mind wanders, bring it back under the control of the Self.", "Song": "Kun Faya Kun - Rockstar","Link":"https://youtu.be/0RDI9CMilhk?si=iAvx-1pkxan-GQ_7"},
        {"Mood": "Emotional", "Quote": "Lift yourself by your own Self; the mind is one’s friend and enemy", "Song": "Chand tare - I am Kalam","link":"https://youtu.be/UVHEvVmqwdo?si=AF-md65C04zjZsLS"},
        {"Mood": "Emotional", "Quote": "Sometimes the heaviest burdens are the ones we carry silently, hidden behind a smile", "Song": "Kabira - yeh jawani hain deewani","link":"https://youtu.be/jHNNMj5bNQw?si=Il49PSlkfyN-7wGv"},
        {"Mood": "Emotional", "quotes":"The heart remembers what the mind tries to forget, and in that memory lies both pain and beauty","song":"Tera yaar hoon mein - sonu ke titu ki sweety","link":"https://youtu.be/C1DucVoyfwY?si=-lLecX4p1sNqQ2Fy"},
        {"Mood": "Emotional", "Quotes":"Some scars are invisible, yet they shape us more than any wound ever could","song":"tujhse naaraz nahi zindagi","link":"https://youtu.be/T2V1lFQ62Is?si=22n_zIC_bz_5X79e"}
    ],
    "Neutral": [
        {"Mood": "Neutral", "Quote": "Be steadfast in yoga; perform your duty, abandoning attachment; equanimity is yoga", "Song": "O Palanhare","link":"https://youtu.be/kbMinfmC3E0?si=G3J6eRrRQWS9lFm9"},
        {"Mood": "Neutral", "Quote": "Cold and heat, pleasure and pain… endure them, O Arjuna", "Song": "Ashayein - ibal","link":"https://youtu.be/CaI0xNLpurM?si=635GwS5oWEHar1zr"},
        {"Mood": "Neutral", "Quote": "Every day is a page in the story of your life; some are quiet, some are loud, but each is worth reading.", "Song": "zindagi kaisi yeh paheli","link":"https://youtu.be/-y6_cFZsMJA?si=vP621yOMfpZH8xhi"},
        {"Mood": "Neutral", "Quote": "Life flows like a river—sometimes calm, sometimes restless, but always moving forward", "Song": "Safarnama","link":"https://youtu.be/7mTDBsdfw88?si=cuRXegtxtvrFxpxo"},
        {"Mood": "Neutral", "Quote": "The mind finds clarity when we simply observe, without needing to change anything", "Song": "o re piya","link":"https://youtu.be/iv7lcUkFVSc?si=eCxqJHQ5CC29Jfij"}
    ],
    "Angry": [
        {"Mood": "Angry", "Quote": "Speak when you are angry and you'll make the best speech you'll ever regret.", "Song": "Bulleya - Ae dil hai mushkil", "link": "https://youtu.be/P3-mbxLvkiE?si=ckg1IGpnoW_c8A2d"},
        {"Mood": "Angry", "Quote": "Anger is one letter short of danger.", "Song": "Bekhayali - kabir singh", "link": "https://youtu.be/NO4BUCFJPqQ?si=Cm-q57sFLAUKBanv"},
        {"Mood": "Angry",  "Quote":"From anger arises delusion… and one falls down from the spiritual platform","song":"jee le zara", "link":"https://youtu.be/gj6KBKzbGDk?si=kGbSoj4B19x7oeCu"},
        {"Mood": "Angry",  "quote":"Anger is a storm; let it pass, or it will drown the calm within you.","Song":"","link":"https://youtu.be/Ax0G_P2dSBw?si=lEzWMWdQvm6TdGaS"},
        {"Mood": "Angry", "Quote": "Don't let anger control you, let it teach you.", "Song": "Jee karda - Badlapur", "link": "https://youtu.be/_2HbGh9dTvk?si=Bmrf3QygVd2xtPkV"}
    ],
    "Love": [
        {"Mood": "Love", "Quote": "You are my today and all of my tomorrows.", "Song": "tum mile - tum mile", "link": "https://youtu.be/8JbEH5rs18Q?si=Q-7j-f3u6RK7bUW2"},
        {"Mood": "Love", "Quote": "Every love story is beautiful, but ours is my favorite.", "Song": "teri meri kahani - gabbar is back", "link": "https://youtu.be/ar5hpVZmGfw?si=K5wbQUq-z-7k7vp1"},
        {"Mood": "Love", "Quote": "Love is composed of a single soul inhabiting two bodies.", "Song": "janam janam - dilwale", "link": "https://youtu.be/g44iifQIFyM?si=eaEzb0Uif557x4Yf"},
        {"Mood": "Love", "quote":"Always think of Me, be devoted to Me, worship Me…","song":"Khuda jane","link":"https://youtu.be/MRysw--JAkM?si=NJEz0WHp9TxYhej6"},
        {"Mood": "Love", "Quote":"Fix your mind on Me… you will come to Me; you are dear to Me","song":"sason ki mala pe","link":"https://youtu.be/-FGYMkL_u-g?si=H7UuwMZPuo1ob3Jw"}
    ],
    "Excited": [
        {"Mood": "Excited", "Quote": "Worker in goodness: free from attachment, fearless, enthusiastic (utsāha), and resolute.", "Song": "kar har maidan fateh","Link":"https://youtu.be/H53LPMYdkl0?si=FrLX327rLOVj4GcO"},
        {"Mood": "Excited", "Quote": "Embrace the thrill—today is yours to conquer.", "Song": "dil dhadkane do","link":"https://youtu.be/Wy43-YD-qcM?si=HXG4DL51_EtevX9i"},
        {"Mood": "Excited", "Quote": "Adventure begins the moment you decide to feel alive.", "Song": "Patakha guddi","link":"https://youtu.be/8HDTS80dlr4?si=A53YbLR8nilT1_tw"},
        {"Mood": "Excited", "quote":"Every heartbeat feels like a drum, and the world is ready for your dance","song":"nachne nu jee karda","link":"https://youtu.be/zgU87U-K14U?si=nPTDrVxIS943Y_AU"},
        {"Mood": "Excited", "Quote":"When joy sparks in your chest, let it light up everything around you","Song":"ude dil befikre","Link":"https://youtu.be/ymDzNv_-hzI?si=8J1-D35lpsPVv3yi"}
    ],
    "Relaxed": [
        {"Mood": "Relaxed", "Quote": "As rivers enter the full, unmoving ocean… such a person alone attains peace", "Song": "pjir le aya dil (reprise)","link":"https://youtu.be/Z93rAu25KqI?si=c1YnLjmwWrBDmCse"},
        {"Mood": "Relaxed", "Quote": "Relaxation is the art of doing nothing and everything at the same time.", "Song": "Namo Namo - Kedarnath","link":"https://youtu.be/dx4Teh-nv3A?si=prJJGbrugrL9BXfv"},
        {"Mood": "Relaxed", "Quote": "Breathe deeply; even the quietest moments have their own melody.", "Song": "dil beparwah re","link":"https://youtu.be/VXOLI_skOnY?si=IYElZbZbBT2C3xq4"},
        {"Mood": "Relaxed", "Quote": "Let the world move around you while you find stillness within", "Song": "Khairiyat","link":"https://youtu.be/_RFUvHlW41A?si=qcubvBoO36UEjwU3"},
        {"Mood": "Relaxed", "Quote": "In the calm, we find clarity, and in clarity, we find ourselves", "Song": "Khamoshiyan","link":"https://youtu.be/qN88U6ZqR-4?si=vb3SsbAiMG4e-o0Z"}
    ],
    "Romantic": [
        {"Mood": "Romantic", "Quote": "Love isn’t just a feeling; it’s the quiet moments that make life magical", "Song": "toota jo kabhi tara","link":"https://youtu.be/EYr9z7uVlLQ?si=rIy4q_U1CsEbNd74"},
        {"Mood": "Romantic", "Quote": "Every heartbeat whispers your name, even when we’re apart", "Song": "tum hi aana","Link":"https://youtu.be/1jDkrhxWLUA?si=9QlutkSFtw0JoskH"},
        {"Mood": "Romantic", "Quote": "Some souls are meant to meet, and ours collided like a spark in the dark", "Song": "javedan he ","link":"https://youtu.be/EvX2ZPtDz-w?si=78vPNmd1Mo_XIVZh"},
        {"Mood": "Romantic", "Quote": "In your eyes, I find the home my heart has always sought", "Song": "tum hi ho","link":"https://youtu.be/P4HYIWfceBQ?si=ijunRGoTZvPhN_Xu"},
        {"Mood": "Romantic", "Quote": "To love you is to see the world in brighter colors and softer light", "Song": "Banjara","link":"https://youtu.be/HDnLm1197oc?si=4vOTTO24Sq3BLpkJ"}
    ]

}

# Create CSV files in table form printing
for mood, entries in mood_data.items():
    df = pd.DataFrame(entries)
    file_path = os.path.join(folder_name, f"{mood}.csv")
    df.to_csv(file_path, index=False)
    print(f"\n {mood} Mood Data:")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
    print(df)

print("\n All CSV files created successfully in the 'mood_data' folder.")
print("\n-------------------------------THANK YOU-------------------------------------")


# Folder name from the CSV generator
FOLDER_NAME = "mood_data"

# READ: Get a random entry from a database CSV
def get_mood(mood_name):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    df = pd.read_csv(file_path)
    return df.sample(1).to_dict(orient="records")[0]  # Returns a random row as a dict

#  CREATE: Add a new entry to a database CSV
def add_entry(mood_name, emoji, quote, song, bg_color):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    new_entry = {
        "Emoji": emoji,
        "Mood": mood_name,
        "Quote": quote,
        "Song": song,
        "Background_Color": bg_color
    }
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])
    df.to_csv(file_path, index=False)
    return f"Entry added to {mood_name} mood."

#  UPDATE: Update entry by index in a database CSV
def update_entry(mood_name, index, emoji=None, quote=None, song=None, bg_color=None):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    df = pd.read_csv(file_path)
    if index < 0 or index >= len(df):
        return "Invalid index."
    if emoji: df.at[index, "Emoji"] = emoji
    if quote: df.at[index, "Quote"] = quote
    if song: df.at[index, "Song"] = song
    if bg_color: df.at[index, "Background_Color"] = bg_color
    df.to_csv(file_path, index=False)
    return f"Entry {index} updated in {mood_name} mood."

#  DELETE: Delete entry by index in a database CSV but with backup already saved
def delete_entry(mood_name, index):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    backup_path = os.path.join(FOLDER_NAME, f"{mood_name}_backup.csv")

    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    
    df = pd.read_csv(file_path)
    if index < 0 or index >= len(df):
        return "Invalid index."

    # Row to be deleted
    deleted_row = df.iloc[[index]]

    # Save to backup file (append mode)
    if os.path.exists(backup_path):
        backup_df = pd.read_csv(backup_path)
        backup_df = pd.concat([backup_df, deleted_row], ignore_index=True)
    else:
        backup_df = deleted_row
    backup_df.to_csv(backup_path, index=False)

    # Delete from main CSV
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(file_path, index=False)

    return f"Entry {index} deleted from {mood_name} mood (backup saved)."

def restore_last_deleted(mood_name):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    backup_path = os.path.join(FOLDER_NAME, f"{mood_name}_backup.csv")

    if not os.path.exists(backup_path):
        return "No backup found."

    backup_df = pd.read_csv(backup_path)
    if backup_df.empty:
        return "Backup is empty."

    # Get last deleted row
    last_row = backup_df.tail(1)

    # Remove it from backup
    backup_df = backup_df.iloc[:-1]
    backup_df.to_csv(backup_path, index=False)

    # Add it back to main CSV
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, last_row], ignore_index=True)
    else:
        df = last_row
    df.to_csv(file_path, index=False)

    return f"Last deleted entry restored to {mood_name} mood."


#  EXTRA: List all moods available in folder
def list_moods():
    return [f.split(".")[0] for f in os.listdir(FOLDER_NAME) if f.endswith(".csv")]

# SEARCH: Search for entries in a mood CSV by keyword or specific field
def search_entries(mood_name, keyword=None, emoji=None, quote=None, song=None, bg_color=None):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    
    df = pd.read_csv(file_path)

    # Apply filters one by one
    if keyword:
        # Search in all columns for keyword
        df = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
    if emoji:
        df = df[df["Emoji"].str.contains(emoji, case=False, na=False)]
    if quote:
        df = df[df["Quote"].str.contains(quote, case=False, na=False)]
    if song:
        df = df[df["Song"].str.contains(song, case=False, na=False)]
    if bg_color:
        df = df[df["Background_Color"].str.contains(bg_color, case=False, na=False)]

    if df.empty:
        return "No matching entries found."
    else:
        return df.to_dict(orient="records")



# List available moods
print("Available moods:", list_moods())

# Add new entry
print(add_entry("Happy", "🤩", "Shine bright like the sun!", "wo kisna hai.mp3", "#FFFF00"))

# Get a random mood entry
print(get_mood("Happy"))

# Update entry at index 0
print(update_entry("Happy", 0, quote="Happiness doubles when shared."))

# Delete entry at index 1
print(delete_entry("Happy", 1))

# to restore the deleted entry
print(restore_last_deleted("Happy"))

