import os
import json
import pronouncing
import subprocess
from pathlib import Path



# Define the wordlist directory
BASE_DIR = Path(__file__).resolve().parent
WORDLIST_DIR = BASE_DIR / "wordlists"
WORDLIST_DIR.mkdir(parents=True, exist_ok=True)

def save_syllable_audio_list(audio_list, filename="syllable_audio.json"):
    filepath = WORDLIST_DIR / filename
    with open(filepath, "w") as f:
        json.dump(audio_list, f, indent=2)


# === CMU Phoneme to IPA ===
CMU_TO_IPA = {
    "AA": "ɑ", "AE": "æ", "AH": "ʌ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ",
    "B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "EH": "ɛ", "ER": "ɝ",
    "EY": "eɪ", "F": "f", "G": "ɡ", "HH": "h", "IH": "ɪ", "IY": "i",
    "JH": "dʒ", "K": "k", "L": "l", "M": "m", "N": "n", "NG": "ŋ",
    "OW": "oʊ", "OY": "ɔɪ", "P": "p", "R": "ɹ", "S": "s", "SH": "ʃ",
    "T": "t", "TH": "θ", "UH": "ʊ", "UW": "u", "V": "v", "W": "w",
    "Y": "j", "Z": "z", "ZH": "ʒ"
}

# === Syllable Vowel Anchors ===
VOWELS = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}

# === Convert phonemes to syllables ===
def phonemes_to_syllables(phonemes):
    syllables = []
    current = ""
    for p in phonemes:
        p_clean = ''.join([c for c in p if not c.isdigit()])
        current += CMU_TO_IPA.get(p_clean, p_clean.lower())
        if p_clean in VOWELS:
            syllables.append(current)
            current = ""
    if current:
        syllables.append(current)
    return syllables

# === Convert phonemes to IPA string ===
def phonemes_to_ipa(phonemes):
    ipa = ""
    for p in phonemes:
        p_clean = ''.join([c for c in p if not c.isdigit()])
        ipa += CMU_TO_IPA.get(p_clean, p_clean.lower()) + " "
    return ipa.strip()

# === Load wordlist from file ===
def load_wordlist(path):
    ext = os.path.splitext(path)[1].lower()
    words = []

    if ext == ".txt":
        with open(path) as f:
            words = [line.strip() for line in f if line.strip()]
    elif ext == ".json":
        with open(path) as f:
            data = json.load(f)
            words = [entry.get("word", "") for entry in data if "word" in entry]
    else:
        raise ValueError("Unsupported file format.")

    return list(set(w.lower() for w in words if w))

# === Generate eSpeak audio ===
def generate_espeak_audio(word, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{word}.wav")
    subprocess.run(["espeak", "-v", "en-us", word, "-w", out_path])
    return out_path

# === Main function ===
def generate_syllable_audio(wordlist_path):
    words = load_wordlist(wordlist_path)
    result = {}

    for word in words:
        phones = pronouncing.phones_for_word(word)
        if not phones:
            result[word] = {"syllables": [word], "ipa": ""}
            continue

        phonemes = phones[0].split()
        syllables = phonemes_to_syllables(phonemes)
        ipa = phonemes_to_ipa(phonemes)

        result[word] = {
            "syllables": syllables,
            "ipa": ipa
        }

        generate_espeak_audio(word, "audio/syllables")

    os.makedirs("data", exist_ok=True)
    with open("data/syllables_with_ipa.json", "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Generated audio for {len(words)} words.")
    print("📁 Saved to: audio/syllables/")
    print("📝 Metadata: data/syllables_with_ipa.json")
