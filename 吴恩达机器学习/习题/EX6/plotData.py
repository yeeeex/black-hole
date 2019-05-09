import matplotlib.pyplot as plt
import numpy as np

def plotData(X, y):
    pos= y==1
    pos=pos.reshape(pos.size)
    neg = y==0
    neg=neg.reshape(neg.size)
    
# Plot Examples
    plt.scatter(X[pos,0], X[pos, 1], marker='+',c='r')
    plt.scatter(X[neg,0], X[neg, 1], marker='o',c='b')
    