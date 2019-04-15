import numpy as np
from lrCostFunction import*
from sigmoid import *
import scipy.optimize as opt
import copy as cp

def oneVsAll(X, y, num_labels, lmd):
    m=X.shape[0]
    n=X.shape[1]
    all_theta=np.zeros((num_labels,n+1))
    init_theta=np.zeros(n+1)
    X=np.c_[np.ones((m,1)),X]
    for  i in np.arange(0,num_labels):
        y_t=cp.deepcopy(y)
        if i==0:
            y_t[y_t!=10]=0
            y_t[y_t==10]=1
        else:
            y_t[y_t!=i]=0
            # y_t[y_t!=1]=0 这一句会导致执行时num_label2时，y[i]==1依然保存着
            y_t[y_t==i]=1
        print("test y_t")
        print (y_t)
        theta_t,cost,*unsed=opt.fmin_cg(f=simple_r_c,fprime=simple_r_g,args=(X,y_t,lmd),x0=init_theta,maxiter=50,disp=False,full_output=True)
        all_theta[i,:]=theta_t
    return all_theta



