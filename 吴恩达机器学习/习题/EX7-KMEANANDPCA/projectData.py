import numpy as np
def projectData(X, U, K):
    Z=np.zeros((X.shape[0],K))
    m=X.shape[0]
    for i in range(m):
        x=X[i,:]
        projection_k=x.dot(U[:,0:K])
        Z[i]=projection_k
    return Z