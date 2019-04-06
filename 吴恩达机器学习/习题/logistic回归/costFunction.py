import numpy as np
import math

def h(X,theta):
    return 1/(1+np.exp(-X.dot(theta)))
#math.log 不能直接对矩阵操作，需要重写，可以使用np库的 log和exp
def costFunction(theta, X, y):
    m=y.size
    J=0
    grad=np.zeros(theta.size)
    values=y.dot(np.log(h(X,theta)))+(1-y).dot(np.log(1-h(X,theta)))#一维数组等于内积
    print("value")
    print(values)
    J=-values/m
    grad=(1/m)*(h(X,theta)-y).dot(X)
    return J,grad



