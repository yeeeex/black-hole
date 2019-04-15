import numpy as np
from sigmoid import *

def return_cost(theta, X, y, lmd):
    J=0
    m=y.size
    J=(-1/m)*(y.dot(np.log(sigmoid(X.dot(theta))))+\
        (1-y).dot(np.log(1-sigmoid(X.dot(theta)))))+\
            (lmd/(2*m))*theta[1:].dot(theta[1:])
    return J

def simple_r_c(theta,*args):
    X,y,lmd=args
    return return_cost(theta,X,y,lmd)

def return_grad(theta, X, y, lmd):
    m=y.size
    grad=np.zeros(theta.size)
    grad=(1/m)*((sigmoid(X.dot(theta))-y).dot(X))+(lmd/m)*(theta)
    grad[0]=grad[0]-(lmd/m)*theta[0]
    return grad

def simple_r_g(theta,*args):
    X,y,lmd=args
    return return_grad(theta,X,y,lmd)

def lrCostFunction(theta, X, y, lmd):
    J=return_cost(theta,X,y,lmd)
    grad=return_grad(theta,X,y,lmd)
    return J,grad
