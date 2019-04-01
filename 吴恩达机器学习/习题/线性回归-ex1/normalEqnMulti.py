import numpy as np

def normal_eqn(x, y):
    tran=np.transpose(x)
    t2=tran.dot(x)
    ni=np.linalg.pinv(t2)
    t3=(ni.dot(tran))
    theta=t3.dot(y)
    return theta
