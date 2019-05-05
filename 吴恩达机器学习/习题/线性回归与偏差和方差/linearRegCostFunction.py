import numpy as np

def h(X,theta):
    return X.dot(theta)
def linearRegCostFunction(X, y, theta, lmd):
    m=y.shape[0]
    J=0
    grad=np.zeros(theta.shape)
    value=h(X,theta)
    y=y.reshape(y.size)
    J+=(value-y).dot(value-y)
    #cost函数有问题
    J/=(2*m)
    J+=(lmd/(2*m))*(theta.dot(theta))
    temp=(value-y).dot(X)+lmd*theta
    temp/=m
    grad=temp
    grad[0]-=(lmd/m)*theta[0]
    return J,grad

