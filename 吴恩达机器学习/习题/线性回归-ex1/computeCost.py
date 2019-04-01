import numpy as np


def h(X,theta):  #线性回归假设函数
    return X.dot(theta)
    
def compute_cost(X, y, theta):


    #初始theta 设为0
    m = y.size #样本数
    cost = 0   #代价函数值
    myh=h(X,theta)  #得到假设函数值  (m,)
    
    cost=(myh-y).dot(myh-y)/(2*m)  #计算代价函数值

    return cost

#need complete
def h_self(x,theta):
    return x.dot(theta) #返回值并不会改变x

def compute_cost_self(x,y,theta):
    m=y.size
    h_value=h_self(x,theta)
    print("-----test h_value-----")
    print(h_value)           #test
    cost=(h_value-y).dot(h_value-y)/(2*m)
    return cost 