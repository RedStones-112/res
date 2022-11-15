import speech_recognition as sr
import os
import sounddevice as sd
import numpy as np
from gtts import gTTS
import pygame
import webbrowser
def speak(text, name):
    tts = gTTS(text=text, lang='ko')
    tts.save(name)
    pygame.mixer.init()
    pygame.mixer.music.load(name)
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
def open_URL(URL):
    webbrowser.get().open(URL)

duration = -1  # seconds

while True:

    present_wave = []
    compare_wave = []

    def print_sound(indata, outdata, frames, time, status):
        #print(np.shape(indata))#(1136,2)
        volume_norm = np.linalg.norm(indata)*10
        print(int(volume_norm))#####
        if int(volume_norm) > 250:

            speak("네 듣고있어요", "check.mp3")
            try :
                text = get_speech()
                print(text)
                if text == "꺼 줘":
                    speak("컴퓨터를 종료합니다", "turnOff.mp3")
                    os.system("shutdown -s -f")
                elif text== "음악":
                    speak("음악리스트를 재생합니다", "programStart.mp3")
                    open_URL("https://www.youtube.com/watch?v=t7MBzMP4OzY&list=PLw_rE4_LEUznWdORlUzK8PICNa-jd8Ly4&index=1")
            except:
                speak("소리가 감지되지 않았습니다", "noSound.mp3")
    with sd.Stream(callback=print_sound):
        sd.sleep(duration)
# microphone에서 auido source를 생성합니다



