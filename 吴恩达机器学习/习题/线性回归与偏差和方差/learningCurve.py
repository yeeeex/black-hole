import numpy as np
from trainLearnReg import *
from linearRegCostFunction import*
def learningCurve(X, y, Xval, yval, lmd):
    m=X.shape[0]
    error_train=np.zeros((m,1))
    error_val=np.zeros((m,1))
    
   
    for i in range(m):
        x=X[:i+1,:]
        y1=y[:i+1]
        theta=trainLinearReg(x,y1,lmd)
        print(theta)
        error_train[i]=linearRegCostFunction(x, y1,theta ,lmd)[0]
        error_val[i]=linearRegCostFunction(Xval, yval,theta, lmd)[0]
    return error_train, error_val


# ====================== YOUR CODE HERE ======================
# Instructions: Fill in this function to return training errors in 
#               error_train and the cross validation errors in error_val. 
#               i.e., error_train(i) and 
#               error_val(i) should give you the errors
#               obtained after training on i examples.
#
# Note: You should evaluate the training error on the first i training
#       examples (i.e., X(1:i, :) and y(1:i)).
#
#       For the cross-validation error, you should instead evaluate on
#       the _entire_ cross validation set (Xval and yval).
#
# Note: If you are using your cost function (linearRegCostFunction)
#       to compute the training and cross validation error, you should 
#       call the function with the lambda argument set to 0. 
#       Do note that you will still need to use lambda when running
#       the training to obtain the theta parameters.
#
# Hint: You can loop over the examples with the following:
#
#       for i = 1:m
#           % Compute train/cross validation errors using training examples 
#           % X(1:i, :) and y(1:i), storing the result in 
#           % error_train(i) and error_val(i)
#           ....
#           
#       end

