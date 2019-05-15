import numpy as np
def computeCentroids(X, idx, K):
    (m,n)=X.shape
    centroids = np.zeros((K, n))
    for i in range(K):
        new_cen=np.zeros(X.shape[1])
        count=0
        for p in range(m):
            if idx[p]==i:
                new_cen+=X[p,:]
                count+=1
        new_cen=new_cen/count
        centroids[i]=new_cen
    return centroids

