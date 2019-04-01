import numpy as np
np.set_printoptions(suppress=True)#浮点输出，而非科学计数法

def featureNormalize(x):
    n=x.shape[1]
    mu=np.zeros(n)
    sigma=np.zeros(n)
    x_new=x
    mu=np.mean(x,axis=0)
    sigma=np.std(x,axis=0)
    x_new=(x_new-mu)/sigma
    return x_new,mu,sigma