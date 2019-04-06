import numpy as np
from costFunction import*

def costfunction_reg(theta,X,y,reglambda):
    j=0
    m=y.size
    grad=np.zeros(theta.size)
    value=(-1)*(y.dot(np.log(h(X,theta)))+(1-y).dot(np.log(1-h(X,theta))))+(reglambda/2)*(theta.dot(theta))
    j=value/m
    grad=(h(X,theta)-y).dot(X)+(reglambda)*(theta)
    #我不知道为何直接在等式中除以M就会报错
    grad=grad/m
    q=reglambda/m
    grad[0]=grad[0]-q*theta[0]
    return j,grad