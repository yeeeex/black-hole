import numpy as np
import scipy.optimize as so

from linearRegCostFunction import*

def trainLinearReg(X, y, lmd):
    initial_theta=np.zeros(X.shape[1])
    def costFunction(t):
        return linearRegCostFunction(X,y,t,lmd)[0]
    def gradFunction(t):
        return linearRegCostFunction(X,y,t,lmd)[1]
    theta=so.fmin_cg(costFunction,initial_theta,gradFunction,maxiter=200)
    return theta

