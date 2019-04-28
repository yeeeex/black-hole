import numpy as np
def debugInitWeights(f_out,f_in):
    W=np.zeros((f_out,f_in+1))
    W = np.reshape(np.sin(range(1, W.size+1)), W.shape)/ 10.0
    return W