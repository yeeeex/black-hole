import matplotlib.pyplot as plt
import numpy as np


def plotDataPoints(X, idx, K):
    m=idx.shape[0]
    t1=[]
    t2=[]
    t3=[]
    for i in range(K):
        temp=idx==i
        counts=0
        for j in range(m):
            if temp[j]==True:
                counts+=1
        if i==0:
            t1=np.zeros((counts,2))       
        if i==1:
            t2=np.zeros((counts,2))   
        if i==2:
            t3=np.zeros((counts,2))   
    t1_pos=0
    t2_pos=0
    t3_pos=0
    for i in range(m):
        if idx[i]==0:
            t1[t1_pos,:]=X[i,:]
            t1_pos+=1
        if idx[i]==1:
            t2[t2_pos,:]=X[i,:]
            t2_pos+=1
        if idx[i]==2:
            t3[t3_pos,:]=X[i,:]
            t3_pos+=1
    plt.scatter(t1[:,0], t1[:, 1], 15, edgecolors='b', marker='o', facecolors='none', lw=0.5)
    plt.scatter(t2[:, 0], t2[:, 1], 15, edgecolors='c', marker='o', facecolors='none', lw=0.5)
    plt.scatter(t3[:, 0], t3[:, 1], 15, edgecolors='g', marker='o', facecolors='none', lw=0.5)
    
