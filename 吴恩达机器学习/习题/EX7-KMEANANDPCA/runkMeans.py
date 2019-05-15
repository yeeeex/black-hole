import numpy as np
from findClosestCentroids import *
from plotProgresskMeans import*
from computeCentroids import*
def runkMeans(X, initial_centroids, max_iters, plot_progress=False):
    (m,n)=X.shape
    K=initial_centroids.shape[0]
    centroids=initial_centroids
    previous_centorids=centroids
    idx=np.zeros((m,1))

    for i in range(max_iters):
        print('K-Means iteration %d/%d...'%(i, max_iters))
        idx = findClosestCentroids(X, centroids)
        if plot_progress:
            plotProgresskMeans(X, centroids, previous_centorids, idx, K, i)
            previous_centroids = centroids
            input('Press enter to continue.\n')
        centroids=computeCentroids(X,idx,K)
    plt.show()
    return centroids,idx
    
def drawLine(p1, p2):
    plt.plot(np.array([p1[0], p2[0]]), np.array([p1[1], p2[1]]), c='black', linewidth=1)

