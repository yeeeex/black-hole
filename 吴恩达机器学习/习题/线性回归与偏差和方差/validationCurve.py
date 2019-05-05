from trainLearnReg import*
import numpy as np
def validationCurve(X, y, Xval, yval):
    lambda_vec = np.array([0,0.001,0.003,0.01,0.03,0.1,0.3,1,3,10])
    error_train=np.zeros((lambda_vec.size,1))
    error_val=np.zeros((lambda_vec.size,1))
    m1=X.shape[0]
    m2=Xval.shape[0]
    for i in range(lambda_vec.size):
        theta=trainLinearReg(X,y,lambda_vec[i])
        y=y.reshape(y.size)
        temp1=X.dot(theta.T)-y
       
        temp1=temp1.reshape(y.size)
        error_train[i]=(temp1.dot(temp1))/(2*m1)
        yval=yval.reshape(yval.size)
        temp2=Xval.dot(theta.T)-yval
        temp2=temp2.reshape(yval.size)
        error_val[i]=temp2.dot(temp2)/(2*m2)
    return lambda_vec,error_train,error_val

