import numpy as np
import os
import cv2 as cv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D#확인용 라이브러리
import random
def Get_range(target_point, data):#중심점들과 목표의 거리 비교
    range1 = sum(np.power(abs(target_point[:,0]-data),2))**0.5
    range2 = sum(np.power(abs(target_point[:,1]-data),2))**0.5
    range3 = sum(np.power(abs(target_point[:,2]-data),2))**0.5
    return np.argmin([range1,range2,range3])
def Get_location(Apple, Banana, Grape, class_list):#과일의 정보를 받고 좌표를 반환 
    sum_data = np.array([0,0,0])

    for i in range(len(class_list)):
        fruit_class = class_list[i][class_list[i].find('_')+1:]
        num = int(class_list[i][:class_list[i].find('_')])
        if fruit_class == '0':
            sum_data = sum_data + Apple[:,num]
            
        elif fruit_class == '1':
            sum_data = sum_data + Banana[:,num]
            
        else:
            sum_data = sum_data + Grape[:,num]
            
    return sum_data/len(class_list)
    
def k_mean(n, k, target_points, Apple, Banana, Grape):
    A = [0,0,0]
    result_list1 = []
    result_list2 = []
    result_list3 = []
    while 1:
        for i in range(n):#거리에따라 각 리스트에 저장
            A[0] = Get_range(target_points,Apple[:,i])
            A[1] = Get_range(target_points,Banana[:,i])
            A[2] = Get_range(target_points,Grape[:,i])
            for j in range(k):
                if A[j] == 0:
                    result_list1.append(str(i)+'_'+str(j))
                elif A[j] == 1:
                    result_list2.append(str(i)+'_'+str(j))
                else:
                    result_list3.append(str(i)+'_'+str(j))
        
        old_target = target_points.copy()
    
        target_points[:,0] = Get_location(Apple, Banana, Grape, result_list1)#
        target_points[:,1] = Get_location(Apple, Banana, Grape, result_list2)
        target_points[:,2] = Get_location(Apple, Banana, Grape, result_list3)
        
        range1 = sum(np.power(abs(target_points[:,0]-old_target[:,0]),2))**0.5
        range2 = sum(np.power(abs(target_points[:,1]-old_target[:,1]),2))**0.5
        range3 = sum(np.power(abs(target_points[:,2]-old_target[:,2]),2))**0.5
        
        if range1 + range2 + range3 <= 5:#전단계의 중점과의 거리총합값이 5이하면 종료 
            return target_points
        

def main():
    k = 3
    n = 30# 각 학습 이미지 개수
    n_test = 10#테스트 이미지 개수
    path = ('./fruits/Apple/','./fruits/Banana/','./fruits/Grape/')#경로
    img_list = np.zeros((3,n),dtype="U10")#문자열 배열생성


    Apple_LearnImg = np.zeros((100,100,3*n))
    Banana_LearnImg = np.zeros((100,100,3*n))
    Grape_LearnImg = np.zeros((100,100,3*n))#학습 이미지 저장 배열


    Apple = np.array([[],[],[]])#RGB 평균값 저장배열
    Banana = np.array([[],[],[]])
    Grape = np.array([[],[],[]])


    for i in range(3):
        img_list[i] =os.listdir(path[i])#파일 경로의 이미지들 이름을 배열에 저장
    for i in range(n):#
        Apple_LearnImg[:,:,i*3:i*3+3] = cv.imread(path[0]+img_list[0][i])#배열에 이미지 저장
        Banana_LearnImg[:,:,i*3:i*3+3] = cv.imread(path[1]+img_list[1][i])
        Grape_LearnImg[:,:,i*3:i*3+3] = cv.imread(path[2]+img_list[2][i])

        
        Apple = np.append(Apple, [[np.average(Apple_LearnImg[:,:,i*3])],[np.average(Apple_LearnImg[:,:,i*3+1])],[np.average(Apple_LearnImg[:,:,i*3+2]) ]], axis = 1)#각 이미지RGB값의 평균값을 저장
        Banana = np.append(Banana, [[np.average(Banana_LearnImg[:,:,i*3])],[np.average(Banana_LearnImg[:,:,i*3+1])],[np.average(Banana_LearnImg[:,:,i*3+2]) ]], axis = 1)
        Grape = np.append(Grape, [[np.average(Grape_LearnImg[:,:,i*3])],[np.average(Grape_LearnImg[:,:,i*3+1])],[np.average(Grape_LearnImg[:,:,i*3+2]) ]], axis = 1)
    

    target_points = np.zeros((k,3))#각 첫 이미지의 좌표를 시작좌표로 설정
    target_points[:,0] = Apple[:,0]
    target_points[:,1] = Banana[:,0]
    target_points[:,2] = Grape[:,0]
    target_points = k_mean(n, k, target_points, Apple, Banana, Grape)

    Query_data = np.array(([],[],[]))
    Random_list = random.sample(range(0,30),10)#0부터 29까지 겹치지않는 무작위숫자 10개를 가진 리스트 생성
    for i in range(n_test):
        Query_data = np.append(Query_data, Apple[:, Random_list[i:i+1]],axis=1)
        Query_data = np.append(Query_data, Banana[:, Random_list[i:i+1]],axis=1)
        Query_data = np.append(Query_data, Grape[:, Random_list[i:i+1]],axis=1)

    Class_1 = np.array([[],[],[]])
    Class_2 = np.array([[],[],[]])
    Class_3 = np.array([[],[],[]])
    
    for i in range(n_test*3):
        Class_num = Get_range(target_points, Query_data[:,i])
        if Class_num == 0:
            Class_1 = np.append(Class_1, Query_data[:,i:i+1], axis=1)
            print(Query_data[:,i])
        elif Class_num == 1:
            Class_2 = np.append(Class_2, Query_data[:,i:i+1], axis=1)
        else:
            Class_3 = np.append(Class_3, Query_data[:,i:i+1], axis=1)


    
    fig = plt.figure(figsize=(6, 6))#확인용 파란점 = 중점3개
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Class_1[:,0], Class_1[:,1], Class_1[:,2], c='red', marker='o', s=15)
    ax.scatter(Class_2[:,0], Class_2[:,1], Class_2[:,2], c='yellow', marker='o', s=15)
    ax.scatter(Class_3[:,0], Class_3[:,1], Class_3[:,2], c='green', marker='o', s=15)
    ax.scatter(target_points[0,:], target_points[1,:], target_points[2,:], c='blue', marker='o', s=15)
    plt.show()

main()





