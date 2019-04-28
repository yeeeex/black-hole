import numpy as np

def computeNumericalG(J,theta):
        numgrad = np.zeros(theta.size)
        perturb = np.zeros(theta.size)
        e = 1e-4
        for p in range(theta.size):
                 perturb[p] = e
                 loss1, grad1 = J(theta - perturb)
                 loss2, grad2 = J(theta + perturb)
                 numgrad[p] = (loss2 - loss1) / (2 * e)
                 perturb[p] = 0
        return numgrad

        