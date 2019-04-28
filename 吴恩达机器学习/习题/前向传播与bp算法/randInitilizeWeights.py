import numpy as np

def randInitializeWeights(L_in, L_out):
    W=np.zeros((L_out,L_in+1))
    epision=0.12
    w=np.array([np.random.uniform(0,2*epision,L_out*(L_in+1))]).reshape((L_out,L_in+1))
    W-=epision
    return W