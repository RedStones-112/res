import speech_recognition as sr
import os
import sounddevice as sd
import numpy as np
from gtts import gTTS
import pygame
def speak(text):
    tts = gTTS(text=text, lang='ko')
    tts.save("gTTSko.wav")
    pygame.mixer.init()
    pygame.mixer.music.load("gTTSko.mp3")
    pygame.mixer.music.play()

def get_speech():
    # 마이크에서 음성을 추출하는 객체
    recognizer = sr.Recognizer()

    # 마이크 설정
    microphone = sr.Microphone(sample_rate=16000)

    # 마이크 소음 수치 반영
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("소음 수치 반영하여 음성을 청취합니다. {}".format(recognizer.energy_threshold))

    # 음성 수집
    with microphone as source:
        print("Say something!")
        result = recognizer.listen(source)
        
        text = recognizer.recognize_google(result, language='ko')
        
    return text
duration = -1  # seconds

while True:

    present_wave = []
    compare_wave = []

    def print_sound(indata, outdata, frames, time, status):
        #print(np.shape(indata))#(1136,2)
        volume_norm = np.linalg.norm(indata)*10
        print(int(volume_norm))
        if int(volume_norm) > 250:
            speak("네 듣고있어요")
            
            try :
                text = get_speech()
                #print(text)
                
            except:
                print("소리가 감지되지 않습니다.")
        else:
            pass
    print("test")
    with sd.Stream(callback=print_sound):
        sd.sleep(duration)
# microphone에서 auido source를 생성합니다



