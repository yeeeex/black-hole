import matplotlib.pyplot as plt
import numpy as np
from plotFeatures import*
def plotFit(min_x, max_x, mu, sigma, theta, p):
    x = np.arange(min_x-15,max_x+25,0.05)
    X_poly = polyFeatures(x,p)
    X_poly -= mu
    X_poly /= sigma
    X_poly = np.c_[np.ones(x.size),X_poly]
    Y_fit = X_poly.dot(theta)
    return x,Y_fit