import pygame.mixer
import time

pygame.mixer.init()

def play_sound(sound_file):
    pygame.mixer.Sound(sound_file).play()

def play_sound_wait(sound_file):
    pygame.mixer.Sound(sound_file).play()
    while pygame.mixer.get_busy():
        time.sleep(0.1)


