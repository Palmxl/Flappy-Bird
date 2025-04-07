import os
import pygame

sprites = {}
audios = {}

# Ruta base segura
BASE_DIR = os.path.dirname(__file__)

def load_sprites():
    path = os.path.join(BASE_DIR, "assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
    return sprites[name]

def load_audios():
    path = os.path.join(BASE_DIR, "assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name):
    audios[name].play()
