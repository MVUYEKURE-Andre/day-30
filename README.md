# day-31

✅ Flash Card App — Read-Me Summary

<img width="1919" height="1024" alt="Screenshot 2025-10-30 035219" src="https://github.com/user-attachments/assets/31435282-f25e-4eec-b8bc-e2bb06b63e52" />

This Python program creates a Flash-Card learning app using Tkinter.
It displays a French word first, then automatically flips after 3 seconds to show the English translation.
If the user marks a word as known, it is removed from the learning list.

📌 Features

✅ Random French word appears on the card
✅ After 3 seconds the card flips to show the English translation
✅ “✓” button → mark word as learned → removes from list
✅ “X” button → skip word
✅ Automatically saves progress in words_to_learn.csv
✅ Uses images for card front/back + buttons

📁 File Requirements

Program expects:

data/french_words.csv
data/words_to_learn.csv    (auto-created)
images/card_front.png
images/card_back.png
images/right.png
images/wrong.png


french_words.csv should contain columns:

French	English
...	...
⚙️ How It Works
✅ Load Data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


If a progress file exists → load it.
Else → load original French word list.

🃏 Display Next Flash Card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


Shows a French word & starts timer to flip card after 3s.

🔄 Flip the Card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


Reveals English translation.

✅ Mark Word as Known
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/5b740821-4f06-4bde-8e08-f508e085299c" />


Removes the known word and saves list so progress stays next time.

🖼 Buttons

✅ Right button → known
❌ Wrong button → skip

Connected to:

unknown_button = Button(..., command=next_card)
known_button = Button(..., command=is_known)

▶ App Start
next_card()
window.mainloop()


Begins showing cards and keeps app running.

✅ Summary Flow

Load list → first time from french_words.csv, later from words_to_learn.csv

Show French word

Auto-flip to English after 3 seconds

Known → remove + save

Not known → another card

Continue…

📚 Libraries Used
Library	Purpose
Tkinter	GUI
Pandas	Data handling
Random	Choose random card
