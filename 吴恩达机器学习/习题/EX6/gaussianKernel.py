import numpy as np
def gaussianKernel(x1, x2, sigma):
    sim = 0
    sim=np.exp(-(x1-x2).dot(x1-x2)/(2*(sigma**2)))
    return sim
