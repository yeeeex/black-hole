from debugInitWeights import*
from nnCostFunction import*
from computeNumericalG import *
def checkNNGradients(lmd):
    input_l_s=3
    hidden_l_s=5
    num_l=3
    m=5
    theta1=debugInitWeights(hidden_l_s,input_l_s)
    theta2=debugInitWeights(num_l,hidden_l_s)
    X=debugInitWeights(m,input_l_s-1)
    y=1+np.mod(np.arange(1,m+1),num_l)
    print(theta1.shape)
    print(theta2.shape)
    X=np.c_[np.ones((X.shape[0],1)),X]
    
    nn_params = np.r_[theta1.ravel(), theta2.ravel()]

    def costFunc(p):
        return nnCostFunction(p,input_l_s,hidden_l_s,num_l,X,y,lmd)
    
    print(nn_params.shape)
    J,grad=costFunc(nn_params)
    numgrad=computeNumericalG(costFunc,nn_params)
    print(numgrad)
    print(np.c_[numgrad,grad])
    #需要测试是grad的问题还是numgrad的问题
    print('The above two columns you get should be very similar.\n(Left-Your Numerical Gradient, Right-Analytical Gradient)\n')
    diff=np.linalg.norm(numgrad-grad)/np.linalg.norm(numgrad+grad)
    print('If your backpropagation implementation is correct, then \n the relative difference will be small (less than 1e-9). \n \
        \nRelative Difference: %g\n'%diff)





