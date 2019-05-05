import numpy as np

def polyFeatures_old(X, p):
    X_poly = np.zeros((np.size(X), p))
    m=X.shape[0]
    if X.size/m!=1:
        n=X.shape[1]
    else:n=0
    for i in range(m):
        if X.size/m!=1:
            for j in range(n):
                for q in range(p):
                    X_poly[i*n+j,q]=X[i,j]**(q+1)
        elif X.size/m ==1:
            for q in range(p):
                X_poly[i,q]==X[i]**(q+1)
    return X_poly

def polyFeatures(X,p):
    m = X.size
    X_poly = np.zeros((m,p))
    for num in range(1,p+1):
        X_poly[:,num-1] = X.flatten() ** num
    return X_poly