import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from displayData import*
from lrCostFunction import *
from oneVsAll import *
from predictOneVsAll import *
import pandas as pd
import copy as cp

np.set_printoptions(threshold = np.inf)
print('Loading and Visualizing Data ...')
data=sio.loadmat("ex3data1.mat")
X=data['X']
y=data['y'].flatten()
np.set_printoptions(precision=5)
print("debug info:")
print(X.shape[0])
print(X.shape[1])  #5000个需要识别字符，每个字符由400个像素点，对应X里有5000个大小为400的VECTOR
print(y.shape[0])  #5000个字符每个字符识别的正确结果,为1，2。。。10中的那一个
print(y[600])




m=y.size
rand_indices = np.random.permutation(range(m))
rX=X[rand_indices[0:100],:]

displayData(rX)

input('Program paused. Press enter to continue.')

print('Testing lrCostFunction() with regularization')

theta_t=np.array([-2,-1,1,2])
#注意，reshape不是转置，而只改变形状
#这里更新一下 np.array([1,2])返回的是一个数组
#np.array([[1,2]])返回的是一个矩阵，c_拼接两个数组是|1    1|
#                                                |2    2|
#r_拼接是[1,2,1,2]正好和矩阵的情况泛着
#同理当用一个矩阵dot一个数组，会自动将数组reshape成(n,1)的形式
X_t=np.c_[np.ones(5),np.arange(1,16).reshape((3,5)).T/10]

y_t=np.array([1,0,1,0,1])
lmd_t=3

J,grad=lrCostFunction(theta_t,X_t,y_t,lmd_t)

print('nCost: %f'%J)
print('Expected cost: 2.534819')
print('Gradients:')
print(grad)
print('Expected gradients:')
print(' 0.146561\n -0.548558\n 0.724722\n 1.398003')

input('Program paused. Press enter to continue.')

# ============ Part 2b: One-vs-All Training ============
print('\nTraining One-vs-All Logistic Regression...')
X_c=cp.deepcopy(X)
y_c=cp.deepcopy(y)

lmd = 0.1
all_theta=oneVsAll(X_c,y_c,10,lmd)
print("theta value")
np.set_printoptions(suppress=True)
print(all_theta)

input('Program paused. Press enter to continue.')

# ================ Part 3: Predict for One-Vs-All ================

pred=predictOneVsAll(all_theta,X)
print("predvalue")
print(y)
print("pred:")
print(pred)
print('Training set accuracy: {}'.format(np.mean(pred == y)*100))
