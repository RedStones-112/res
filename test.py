import speech_recognition as sr
import os
import sounddevice as sd
import numpy as np
from gtts import gTTS
import playsound
import pygame
import time
def speak(text):
    tts = gTTS(text=text, lang='ko')
    tts.save("gTTSko.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("gTTSko.mp3")
    pygame.mixer.music.play()


    
speak("네 듣고있어요")
time.sleep(2)