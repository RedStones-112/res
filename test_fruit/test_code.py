import numpy as np
import os
import matplotlib.pyplot as plt
import cv2 as cv

test = np.array([[5,3,5],[7,5,4],[6,0,5]])
test2 = np.array([['7','7','7'],['8','8','8'],['9','9','9']])
old = np.array([[7,7,7],[8,8,8],[9,9,9]])
L = np.array([[],[],[]])
L = np.append(L, old[:,0])
print(L.shape)