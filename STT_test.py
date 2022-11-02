import speech_recognition as sr
import os
import time
import schedule
# microphone에서 auido source를 생성합니다
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
try:
    print("Google Speech Recognition thinks you said : " + r.recognize_google(audio, language='ko'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



'''
if r.recognize_google(audio, language='ko') == "마이크 테스트":
    print("hi")
    if r.recognize_google(audio, language='ko') == "마이크 테스트":
        os.system("shutdown -s -t 1")
else:
    pass
'''
