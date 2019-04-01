import numpy as np

def h(x,theta):
    return x.dot(theta)

def computeCostMulti(x,y,theta):
    m=y.size
    value=h(x,theta)
    j=0.0
    j=(value-y).dot(value-y)/(2*m)
    return j
