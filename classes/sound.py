import pygame
from pygame import mixer
class Sound:
    pygame.mixer.init()
    initialize the mixer module
    init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE) -> None