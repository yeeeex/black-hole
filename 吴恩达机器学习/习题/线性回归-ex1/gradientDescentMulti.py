import numpy as np
from computeCostMulti import *

def gradientDescentMulti(x, y, theta, alpha, num_iters):
    m=y.size
    j_history=np.zeros(num_iters)
    for i in range(0,num_iters):
        theta=theta-(alpha/m)*((h(x,theta)-y).dot(x))
        j_history[i]=computeCostMulti(x,y,theta)
        print(j_history[i])
    return theta,j_history
