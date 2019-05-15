import numpy as np
import numpy.linalg as la
def pca(X):
    (m,n)=X.shape
    U=np.zeros(n)
    S=np.zeros(n)
    sigma=(X.T).dot(X)/m
    U,S,V=la.svd(sigma)
    return U,S


    