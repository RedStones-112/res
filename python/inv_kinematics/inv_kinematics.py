import numpy as np
import math
import matplotlib.pyplot as plt






point_zero = [0,0]

point = [10,0]

def kinematics(l,c):# 
    z = [0,0,0,0]
    x = [0,0,0,0]
    y = [0,0,0,0]
    x[1] = x[0] + math.cos(c[0])*l[0]#
    y[1] = z[0] + math.sin(c[0])*l[0]#
    #x[2] = x[0] + math.cos(c[0])*l[0] + math.cos(c[0] + c[1])*l[1]# end x
    #y[2] = y[0] + math.sin(c[0])*l[0] + math.sin(c[0] + c[1])*l[1]# end y
    #x[3] = x[0] + math.cos(c[0])*l[0] + math.cos(c[0] + c[1])*l[1] + math.cos(c[0] + c[1] + c[2])*l[2]# end x
    #y[3] = y[0] + math.sin(c[0])*l[0] + math.sin(c[0] + c[1])*l[1] + math.sin(c[0] + c[1] + c[2])*l[2]# end y
    return x,y,z

def invkinematics(l,x,y):
    
    Cos_c2 = ((x[2]**2 + y[2]**2 - l[0]**2 - l[1]**2 )/2/l[0]/l[1])
    Sin_c2 = math.sqrt(1-Cos_c2**2)#**(1/2)
    c2 = math.atan2(Sin_c2,Cos_c2)
    c1 = math.atan2(y[2], x[2]) - math.atan2(l[0] + l[1] * Cos_c2, l[1] * Sin_c2)
    
    return c1,c2
    
def main():
    c = np.zeros((3, 1))
    l = [5, 10, 10]
    tic = 0.1
    time = 0
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    
    while time <= 1: 
        x,y,z = kinematics(l,c)
        ax.plot(x, y, z,'g')
        ax.scatter(x, y, z,'g', 20)
        #sc1, sc2 = invkinematics(l,x,y)
        #print(c[2],sc2)
        c[0] += 0.1
        c[1] += 0.1
        c[2] += 0.1
        time += tic
    plt.show()
main()