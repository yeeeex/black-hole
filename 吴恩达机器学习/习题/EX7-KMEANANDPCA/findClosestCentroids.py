import numpy as np

def findClosestCentroids(X, centroids):
    K=centroids.shape[0]
    idx=np.zeros((X.shape[0],1))
    m1=X.shape[0]
    m2=centroids.shape[0]
    for i in range(m1):
        min=np.inf
        pos=-1
        for j in range(m2):
            temp=X[i,:]-centroids[j,:]
            dist=temp.dot(temp)
            if dist<min:
                min=dist
                pos=j
            else: continue
        idx[i]=pos
    return idx
        
