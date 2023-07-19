from PIL import ImageGrab
import os
import cv2
import pyautogui
import keyboard
import time
import pynput
import numpy as np
import serial
PORT = 'COM6'
BaudRate = 9600
ARD = serial.Serial(PORT,BaudRate)

pushbutton1 = str(1)
pushbutton2 = str(2)

Trans1 = "Q" + pushbutton1
Trans1 = Trans1.encode('utf-8')

Trans2 = "Q" + pushbutton2
Trans2 = Trans2.encode('utf-8')

# full screen
screen_w = 1920
screen_h = 1080
pix_w = 8
pix_h = 80
keyboard_button = pynput.keyboard.Controller()
keyboard_key = pynput.keyboard.Key
end = 0
def press_key():
    pass
#img_full = ImageGrab.grab()
# crob screen
#img_crop = ImageGrab.grab([0,0,800,600])
#img_crop = ImageGrab.grab([screen_w/2-80 ,screen_h/2-80 ,screen_w/2+80 ,screen_h/2+80])
# img show
#img_crop = ImageGrab.grab([screen_w/2-pix_w ,screen_h/2-pix_h ,screen_w/2+pix_w ,screen_h/2])
#img_tt   = ImageGrab.grab([screen_w/2-pix_w ,screen_h/2-pix_h ,screen_w/2+pix_w ,screen_h/2]).load()
#img_crop.show()
#pyautogui.press('w')
#pyautogui.keyUp('w')#키때기
#pyautogui.keyDown('w')

#time.sleep(1000)

while cv2.waitKey(1)  != 27:
    if keyboard.is_pressed('esc'):
        break
    time.sleep(0.01)
    
    

    img_crop = np.array(ImageGrab.grab([screen_w/2-pix_w ,screen_h/2-pix_h ,screen_w/2+pix_w ,screen_h/2]))
    img = cv2.cvtColor(img_crop, cv2.COLOR_BGR2HSV)

    
    imgThreshLow = cv2.inRange(img, (0, 155, 155), (18, 255, 255))#이진화 
    imgThreshHigh = cv2.inRange(img, (165, 155, 155), (179, 255, 255))#이진화 

    imgThresh = cv2.add(imgThreshLow, imgThreshHigh)#이진화 합침
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6)) # 가로 , 세로 
    ct = cv2.dilate(imgThresh,se)#팽창
    ct = cv2.erode(ct,se)#침식
    cv2.imshow('win',ct)
    if ct.sum()/255 < 1000:
        ARD.write(Trans1)
        time.sleep(0.2)
        ARD.write(Trans2)
        time.sleep(5)
        end = 1
        print("w",ct.sum()/255)
        
    else:
        ARD.write(Trans2)
        print("s",ct.sum()/255)
    
    if end == 1:
        #time.sleep(2)
        ARD.write(Trans1)
        time.sleep(0.2)
        ARD.write(Trans2)
        print('t')
        end = 0
    else:
        pass







