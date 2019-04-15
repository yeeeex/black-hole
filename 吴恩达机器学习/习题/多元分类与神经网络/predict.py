import numpy as np
from sigmoid import *

def predict(Theta1, Theta2, X):
    m=X.shape[0]
    numbel_labels=Theta2.shape[0]
    p=np.zeros((m,1))
    X=np.c_[np.ones((m,1)),X]
    z1=X.dot(Theta1.T)
    a2=sigmoid(z1)
    a2=np.c_[np.ones((z1.shape[0],1)),a2]
    z3=a2.dot(Theta2.T)
    a3=sigmoid(z3)
    p=np.argmax(a3,axis=1)
    #这一步我其实没懂为啥会返回的位置比原来小1即p为何要加一
    #我只是观察数据出来应该加，但是为何我在predictonvsall里没加也返回了正确的数据
    #我想应该是因为运用神经网络求出来的预测结果，theta时给定好了的，可能会直接将
    #0映射到10，而不用人工修改
    p=p+1  
    

    return p
    


