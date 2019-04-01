import numpy as np

def normal_eqn(x, y):
    theta=np.zeros(x.shape[1])
    theta=np.linalg.pinv(x.T.dot(x)).dot(x.T).dot(y)
    return theta