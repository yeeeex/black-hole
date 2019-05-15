import numpy as np
def recoverData(Z, U, K):
    X_rec=np.zeros((Z.shape[0],U.shape[0]))
    m=Z.shape[0]
    n=U.shape[0]
    for i in range(m):
        v=Z[i,:]
        for j in range(n):
            recovered_j=v.dot(U[j,0:K])
            X_rec[i,j]=recovered_j
    
    return X_rec