import numpy as np
import math
import matplotlib.pyplot as plt






point_zero = [0,0]

point = [10,0]

def kinematics(l1,l2,c1,c2,c3):
    z = 0
    x = [0,0,0]
    y = [0,0,0]
    x[1] = math.cos(c2)*l1# mid x
    y[1] = math.sin(c2)*l1# mid y
    x[2] = math.cos(c2)*l1 + math.cos(c2+c3)*l2# end x
    y[2] = math.sin(c2)*l1 + math.sin(c2+c3)*l2# end y
    return x,y

def invkinematics(x,y):
    pass
def main():
    #x,y = kinematics(l[0],l[1],c[0],c[1],c[2])
    #plt.plot(x,y,'g')
    #plt.scatter(x,y,20,'g')
    c = np.zeros((3, 1))
    l = [5, 10]
    tic = 0.1
    time = 0
    
    
    
    while time <= 1: 
        x,y = kinematics(l[0],l[1],c[0],c[1],c[2])
        plt.plot(x,y,'g')
        plt.scatter(x,y,20,'g')
        print(x,y)
        c[1] += 0.1
        c[2] += 0.1
        time += tic
    plt.show()
main()