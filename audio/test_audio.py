import pygame
import time

audio_path = "/home/kali/LitBuddy/audio/ai.mp3"

pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

print(f"🔊 Playing: {audio_path}")
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
