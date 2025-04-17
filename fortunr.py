# fortune.py (v1.1)

import random

print("🔮 Welcome to Parth Pandya's Fortune Teller (21JE10635) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "✨ Great things await you, Aryan! Keep smiling.",
        "🌈 Joy surrounds you today. Embrace it!"
    ],
    "sad": [
        "💙 This too shall pass. Aryan believes in you.",
        "🌧️ Rainy days make the flowers bloom. Stay hopeful."
    ],
    "neutral": [
        "😐 Peace and clarity are within reach.",
        "📘 Embrace simplicity; profound truths hide there."
    ],
    "stressed": [
        "🧘‍♂️ Breathe in calm, exhale stress. Aryan's got your back.",
        "🔥 Stress tests your strength—you're passing with grace."
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("🤔 Sorry, I don't recognize that mood.")
