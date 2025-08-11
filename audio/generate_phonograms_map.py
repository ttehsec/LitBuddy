import os
import json

# Full phonogram list (same as used in audio generation)
phonogram_list = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "qu", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "ai", "ay", "ea", "ee", "ei", "ey", "igh", "ie", "oa", "oe", "oo", "ou", "ow", "oy", "oi", "ue", "ui",
    "ar", "er", "ir", "or", "ur", "al", "au", "aw", "eigh", "ear", "air", "ure",
    "ch", "sh", "th", "wh", "ph", "gh", "ck", "dge", "tch", "gn", "kn", "wr", "mb", "gu", "ng", "nk"
]

# Set your audio folder path
audio_folder = "/home/kali/LitBuddy/audio/phonograms"

# Build the map
phonics_audio_map = {
    phonogram: os.path.join(audio_folder, f"{phonogram}.mp3")
    for phonogram in phonogram_list
}

# Save to JSON
with open("phonics_audio_map.json", "w") as f:
    json.dump(phonics_audio_map, f, indent=4)

print("✅ phonics_audio_map.json created successfully.")
