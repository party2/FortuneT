# fortune.py (v1.0)

print("🔮 Welcome to Parth Pandya's Fortune Teller (21JE0635) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Aryan! Keep smiling. ✨")
elif mood == "sad":
    print("💙 Your fortune: Better days are coming, stay strong.")
elif mood == "neutral":
    print("😐 Your fortune: Sometimes peace lies in simplicity.")
else:
    print("🤔 Sorry, I don't recognize that mood.")
