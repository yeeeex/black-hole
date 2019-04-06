import numpy as np
import matplotlib.pyplot as plt

def plotData(X,y):
    p=plt.figure(1)

    pos=X[y==1]
    print("test y==1")
    print(X[y==1]) #会将所有y==1对应的X分割出来，记住就好了
    neg=X[y==0]
    plt.scatter(pos[:,0],pos[:,1],marker='+',c='red',label='Admitted')
    plt.scatter(neg[:,0],neg[:,1],marker='o',c='blue',label='Not Admitted')