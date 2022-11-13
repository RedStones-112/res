import speech_recognition as sr
import os
import sounddevice as sd
import numpy as np
from gtts import gTTS
import playsound
import pygame
import time
def speak(text,name):
    tts = gTTS(text=text, lang='ko')
    tts.save(name)
    playsound.playsound(name)
    '''
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
'''


    
speak("네 듣고있어요","gTTSko.mp3")
time.sleep(1)