import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("ă-ā-ä.wav")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)
