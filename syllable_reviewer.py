import nltk
import json
import os
from gtts import gTTS
import time



# Setup CMU Pronouncing Dictionary
nltk.download('cmudict')
from nltk.corpus import cmudict
cmu = cmudict.dict()

# Optional: Add intuitive variants
intuitive = {
    "computer": ["com-pyu-ter", "kuhm-pyoo-ter", "kəm-pjuː-tər"],
    "about": ["uh-bout", "ə-bowt", "a-bout"],
    "action": ["ak-shun", "ak-shən", "a-kshun"],
    "addition": ["uh-di-shun", "ə-dish-ən", "a-dish-un"],
    "aim": ["aym", "eym"],
    "allow": ["uh-low", "ə-lau"],
    "alloy": ["al-oy", "a-loy"],
    "aloe": ["al-oh", "a-loh"],
    "alphabet": ["al-fuh-bet", "al-fa-bet", "æl-fə-bɛt"]
}

def play_text(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "temp.mp3"
    tts.save(filename)
    os.system(f"mpg123 {filename}")
    time.sleep(1.2)  # brief pause after playback
    os.remove(filename)

# 🔍 Generate syllable options
def get_syllable_options(word):
    word = word.lower()
    options = set()

    # CMU-based syllables
    if word in cmu:
        for pron in cmu[word]:
            syllables = []
            current = ""
            for phoneme in pron:
                current += phoneme + " "
                if phoneme[-1].isdigit():  # Vowel sound
                    syllables.append(current.strip())
                    current = ""
            if current:
                syllables.append(current.strip())
            options.add("-".join(syllables))

    # Add intuitive variants
    if word in intuitive:
        options.update(intuitive[word])

    return list(options)

# 🧠 Interactive reviewer
def review_word(word, options):
    print(f"\n🔍 Word: {word}")
    
    # 🔊 Play full word first
    play = input(f"🔊 Hear the full word '{word}'? (y/n): ").strip().lower()
    if play == "y":
        play_text(word)

    print("📖 Syllable Options:")
    for i, opt in enumerate(options):
        print(f"  {i+1}. {opt}")
        play = input(f"🔊 Hear option {i+1}? (y/n): ").strip().lower()
        if play == "y":
            play_text(opt.replace("-", " "))

    choice = input("✅ Choose the best option (1/2/3/edit/skip): ").strip().lower()
    
    if choice == "skip":
        return None
    elif choice == "edit":
        custom = input("✏️ Enter your custom syllables: ").strip()
        play = input("🔊 Hear your custom version? (y/n): ").strip().lower()
        if play == "y":
            play_text(custom.replace("-", " "))
        return custom
    elif choice.isdigit() and 1 <= int(choice) <= len(options):
        return options[int(choice)-1]
    else:
        print("❌ Invalid choice. Skipping.")
        return None



# 📝 Main loop
def run_reviewer(word_list):
    final_syllables = {}
    for word in word_list:
        options = get_syllable_options(word)
        if not options:
            print(f"\n⚠️ No syllable options found for '{word}'")
            continue
        selected = review_word(word, options)
        if selected:
            final_syllables[word] = selected
        else:
            print("❌ Marked for later review.")

    # Save to JSON
    with open("custom_syllables.json", "w") as f:
        json.dump(final_syllables, f, indent=2)
    print("\n✅ Review complete. Saved to custom_syllables.json")

# 🧪 Example usage
if __name__ == "__main__":
    words_to_review = ["computer", "about", "action", "addition", "aim", "allow", "alloy", "aloe", "alphabet"]
    run_reviewer(words_to_review)
