import numpy as np

def featureNormalize(X):
    mu=X.mean(axis=0)
    X_norm=X-mu
    sigma = np.std(X, 0, ddof=1)
    X_norm=X_norm/sigma
    return X_norm,mu,sigma
