import os
import subprocess

phonogram_text_map = {
    "ai": "ay",
    "ee": "see",
    "ch": "chip"
}

output_dir = "/home/kali/LitBuddy/audio/phonograms"
os.makedirs(output_dir, exist_ok=True)

for phonogram, text in phonogram_text_map.items():
    wav_path = os.path.join(output_dir, f"{phonogram}.wav")

    print(f"🔄 Generating {phonogram} using text: '{text}'")

    cmd = [
        "espeak",
        "-v", "en-us",
        "-w", wav_path,
        text
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ Error generating {phonogram}: {result.stderr}")
    elif os.path.exists(wav_path):
        print(f"✅ Created: {wav_path}")
    else:
        print(f"⚠️ No file created for {phonogram} — check if espeak supports -w")
