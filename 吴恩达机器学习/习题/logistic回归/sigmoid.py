import numpy as np

def sigmoid(z):
    np.zeros(np.size(z))
    g=1/(1+np.exp(-z))
    return g
