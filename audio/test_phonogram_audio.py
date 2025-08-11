import pygame
import time
import os

# Path to the phonogram file you want to test
audio_path = "/home/kali/LitBuddy/audio/phonograms/ai.mp3"

# Check if the file exists
if not os.path.isfile(audio_path):
    print(f"❌ File not found: {audio_path}")
    exit()

# Initialize pygame mixer
pygame.mixer.init()

try:
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    print(f"🔊 Playing: {audio_path}")
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
except pygame.error as e:
    print(f"❌ Playback error: {e}")
