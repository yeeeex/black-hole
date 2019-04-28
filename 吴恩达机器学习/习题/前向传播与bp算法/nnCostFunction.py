import numpy as np
from sigmoid import *
from sigmoidGradient import *
from debugcode import *

def h(X,theta1,theta2):
    
    temp=sigmoid(X.dot(theta1.T))
    temp=np.r_[np.ones((1,)),temp]
   
    return sigmoid(temp.dot(theta2.T))
#inputlayers=400
#hidden=25
#number=10
def nnCostFunction(nn_params,input_layer_size,hidden_layer_size,num_label,X, y, lmd):
#------------------part 1 start------------------------------------------------------
    np.set_printoptions(suppress=True,threshold=np.inf)
    Theta1=nn_params[0:hidden_layer_size*(input_layer_size+1)].reshape((hidden_layer_size,input_layer_size+1))
    Theta2=nn_params[hidden_layer_size*(input_layer_size+1):].reshape((num_label,hidden_layer_size+1))
    #被错误的转置了，以前t1的纵轴变横轴了
  
    m=X.shape[0]
    J=0
    Theta1_grad=np.zeros(Theta1.shape)
    Theta2_grad=np.zeros(Theta2.shape)
    values=np.zeros((X.shape[0],num_label))
    Thetas_one=Theta1[:,1:].reshape(hidden_layer_size*input_layer_size)
    
    
    Thetas_two=Theta2[:,1:].reshape(hidden_layer_size*num_label)
    
    for i in np.arange(X.shape[0]):
        values[i,:]=h(X[i,:],Theta1,Theta2)
    new_y=np.zeros((X.shape[0],num_label))
    
    for i in np.arange(y.size):
        new_y[i,y[i]-1]=1
    
    for i in np.arange(m):
        temp1=new_y[i,:].dot(np.log(values[i,:]))+(1-new_y[i,:]).dot(np.log(1-values[i,:]))
        J+=temp1
    J=-J/m+(lmd/(2*m))*(Thetas_one.dot(Thetas_one)+Thetas_two.dot(Thetas_two))
    error_ouput=values-new_y
    error_hidden=(error_ouput.dot(Theta2))*(sigmoidGradient(np.c_[np.ones((m,1)),X.dot(Theta1.T)]))
    
    delta_2=np.zeros((Theta2.shape))
  
    temp_a=sigmoid(np.c_[np.ones((m,1)),X.dot(Theta1.T)])
    
    delta_2+=(error_ouput.T).dot(temp_a)
    
    delta_2/=m
    delta_1=np.zeros(Theta1.shape)
    delta_1+=(error_hidden[:,1:].T).dot(X)
    #J的计算有问题
    delta_1/=m
    print(delta_1.shape)
    delta_1[:,1:]+=(lmd/m)*Theta1[:,1:]
    delta_2[:,1:]+=(lmd/m)*Theta2[:,1:]
    Theta1_grad=delta_1
    Theta2_grad=delta_2
    grad=np.hstack((Theta1_grad.ravel(),Theta2_grad.ravel()))
    #解决grad返回组合grad1,grad2得问题
    return J,grad
#--------------------------------part 1 end-------------------------------------------
