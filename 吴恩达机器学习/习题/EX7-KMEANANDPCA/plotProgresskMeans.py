from plotDataPoints import*

def plotProgresskMeans(X, centroids, previous, idx, K, i):
    plotDataPoints(X,idx,K)
    plt.scatter(centroids[:, 0], centroids[:, 1],marker='x', s=60, lw=3, edgecolor='k')
    for j in range(len(centroids)):
        plt.plot([centroids[j,0], previous[j,0]],[centroids[j,1], previous[j,1]],c='y')
    
