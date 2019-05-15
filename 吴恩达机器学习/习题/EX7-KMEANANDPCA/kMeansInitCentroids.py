import numpy as np
def kMeansInitCentroids(X, K):
    centroids=np.zeros((K,X.shape[1]))
    pos=np.random.permutation(X.shape[0])
    for i in range(K):
        centroids[i,:]=X[pos[i],:]
    return centroids


