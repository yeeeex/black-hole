import numpy as np
from costFunction import *

def predict(theta,X):
    m=X.shape[0]
    p=np.zeros((m,1))
    p=h(X,theta)
    for i in range(0,p.size):
        if p[i]>=0.5:
            p[i]=1
        else:
            p[i]=0
    return p