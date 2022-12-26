import numpy as np
import os
import matplotlib.pyplot as plt
import cv2 as cv
from mpl_toolkits.mplot3d import Axes3D#확인용 라이브러리

def Learn_data(target_point, data):#중심점들과 목표의 거리 비교
    range1 = sum(np.power(abs(target_point[:,0]-data),2))**0.5
    range2 = sum(np.power(abs(target_point[:,1]-data),2))**0.5
    range3 = sum(np.power(abs(target_point[:,2]-data),2))**0.5
    
    return np.argmin([range1,range2,range3])

k = 3
n = 30# 각 학습 이미지 개수
path = ('./fruits/Apple/','./fruits/Banana/','./fruits/Grape/')#경로
img_list = np.zeros((3,n),dtype="U10")#문자열 배열생성


Apple_LearnImg = np.zeros((100,100,3*n))
Banana_LearnImg = np.zeros((100,100,3*n))
Grape_LearnImg = np.zeros((100,100,3*n))#학습 이미지 저장 배열

Apple_LearnImg_HSV = np.zeros((100,100,3*n))
Banana_LearnImg_HSV = np.zeros((100,100,3*n))
Grape_LearnImg_HSV = np.zeros((100,100,3*n))#흑백 학습 이미지 저장 배열


Apple = np.array([[],[],[]])#RGB 평균값 저장배열
Banana = np.array([[],[],[]])
Grape = np.array([[],[],[]])


for i in range(3):
    img_list[i] =os.listdir(path[i])#파일 경로의 이미지들 이름을 배열에 저장
for i in range(n):
    Apple_LearnImg[:,:,i*3:i*3+3] = cv.imread(path[0]+img_list[0][i])#배열에 이미지 저장
    Banana_LearnImg[:,:,i*3:i*3+3] = cv.imread(path[1]+img_list[1][i])
    Grape_LearnImg[:,:,i*3:i*3+3] = cv.imread(path[2]+img_list[2][i])

    Apple_LearnImg_HSV[:,:,i*3:i*3+3] = (cv.cvtColor(cv.imread(path[0]+img_list[0][i]), cv.COLOR_BGR2HSV))#HSV로 변환
    Banana_LearnImg_HSV[:,:,i*3:i*3+3] = (cv.cvtColor(cv.imread(path[1]+img_list[1][i]), cv.COLOR_BGR2HSV))
    Grape_LearnImg_HSV[:,:,i*3:i*3+3] = (cv.cvtColor(cv.imread(path[2]+img_list[2][i]), cv.COLOR_BGR2HSV))


    Apple = np.append(Apple, [[np.average(Apple_LearnImg[:,:,i])],[np.average(Apple_LearnImg[:,:,i+1])],[np.average(Apple_LearnImg[:,:,i+2]) ]], axis = 1)#각 이미지RGB값의 평균값을 저장
    Banana = np.append(Banana, [[np.average(Banana_LearnImg[:,:,i])],[np.average(Banana_LearnImg[:,:,i+1])],[np.average(Banana_LearnImg[:,:,i+2]) ]], axis = 1)
    Grape = np.append(Apple, [[np.average(Apple_LearnImg[:,:,i])],[np.average(Apple_LearnImg[:,:,i+1])],[np.average(Apple_LearnImg[:,:,i+2]) ]], axis = 1)
    

target_points = np.random.rand(k,3)*255#랜덤한 값을 가지는 3차원좌표 3개 생성


for i in range(n):#미완성 부분
    result = Learn_data(target_points,Apple[:,i])
    
    

# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(Apple[0,:], Apple[1,:], Apple[2,:], c='red', marker='o', s=15, cmap='Greens')
# plt.show()







