import numpy as np
import scipy.io as sio
import random as rd
from DisplayData import *
import scipy.io as sio
from nnCostFunction import*
from sigmoidGradient import*
from randInitilizeWeights import*
from checkNNGradient import *
from scipy.optimize import minimize
from predict import*
num_labels=10
input_layer_size=400
hidden_layer_size=25

print('Loading and Visualizing Data ...')
data=sio.loadmat("ex4data1.mat")
X=data['X']
y=data['y'].flatten()

m=X.shape[0]
indices=np.random.permutation(m)
rx=X[indices[0:100],:]

displayData(rx)

print('Loading Saved Neural Network Parameters ...')
np.set_printoptions(suppress=True,threshold=np.inf)
weights=sio.loadmat("ex4weights.mat")
Theta1=weights['Theta1']
Theta2=weights['Theta2']
print(Theta1.shape)
print(Theta2.shape)
T1=Theta1.reshape((Theta1.shape[0]*Theta1.shape[1]))
T2=Theta2.reshape((Theta2.shape[0]*Theta2.shape[1]))
nn_params = np.r_[Theta1.ravel(), Theta2.ravel()]
print(Theta1[0,:])
print(Theta1.shape)
print(nn_params[0:401])
print('\nFeedforward Using Neural Network ...')

lmd=0
print(nn_params.shape)
X=np.c_[np.ones((X.shape[0],1)),X]
J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lmd)[0]
np.set_printoptions(suppress=True)
print(J)
print('Cost at parameters (loaded from ex4weights):%f\n(this value should be about 0.287629)'%J)

print('Program paused. Press enter to continue.')

lmd = 1

J,grad = nnCostFunction(nn_params, input_layer_size, hidden_layer_size,num_labels, X, y, lmd)

print('Cost at parameters (loaded from ex4weights): %f \n(this value should be about 0.383770)'%J)

print('Program paused. Press enter to continue.')

print('\nEvaluating sigmoid gradient...')
g=sigmoidGradient(np.array([1,-0.5,0,0.5,1]))
print('Sigmoid gradient evaluated at [1 -0.5 0 0.5 1]:')
print(g)
print('\n')
input('Program paused. Press enter to continue.')

lmd=3
debug_J  = nnCostFunction(nn_params, input_layer_size,hidden_layer_size, num_labels, X, y, lmd)[0]

print('\n\nCost at (fixed) debugging parameters (w/ lambda = 10): %f \
         \n(this value should be about 0.576051)\n'%debug_J)

print('Initializing Neural Network Parameters ...')

init_theta1= randInitializeWeights(input_layer_size, hidden_layer_size)
init_theta2= randInitializeWeights(hidden_layer_size, num_labels)
init_nn_params=np.r_[init_theta1.reshape((init_theta1.shape[0]*init_theta1.shape[1])),\
    init_theta2.reshape((init_theta2.shape[0]*init_theta2.shape[1]))]

checkNNGradients(0)
input('\nProgram paused. Press enter to continue.')

print('\nChecking Backpropagation (w/ Regularization) ... ')

lmd=3
checkNNGradients(3)
debug_J  = nnCostFunction(nn_params, input_layer_size,hidden_layer_size, num_labels, X, y, lmd)[0]

print('\n\nCost at (fixed) debugging parameters (w/ lambda = 10): %f \
         \n(this value should be about 0.576051)\n'%debug_J)

input('Program paused. Press enter to continue.\n')

print('Training Neural Network... ')

#  After you have completed the assignment, change the MaxIter to a larger
#  value to see how more training helps.
# options = optimset('MaxIter', 50)

#  You should also try different values of lambda
Lambda = 1

costFunc = lambda p: nnCostFunction(p, input_layer_size, hidden_layer_size, num_labels, X, y, Lambda)[0]
gradFunc = lambda p: nnCostFunction(p, input_layer_size, hidden_layer_size, num_labels, X, y, Lambda)[1]

result = minimize(costFunc, nn_params, method='CG', jac=gradFunc, options={'disp': True, 'maxiter': 50.0})
nn_params = result.x
cost = result.fun

# Obtain Theta1 and Theta2 back from nn_params
Theta1 = np.reshape(nn_params[:hidden_layer_size * (input_layer_size + 1)],
                   (hidden_layer_size, input_layer_size + 1), order='F').copy()
Theta2 = np.reshape(nn_params[hidden_layer_size * (input_layer_size + 1):],
                   (num_labels, (hidden_layer_size + 1)), order='F').copy()

input("Program paused. Press Enter to continue...")


## ================= Part 9: Visualize Weights =================
#  You can now "visualize" what the neural network is learning by 
#  displaying the hidden units to see what features they are capturing in 
#  the data.

print('Visualizing Neural Network...' )

displayData(Theta1[:, 1:])

input("Program paused. Press Enter to continue...")

## ================= Part 10: Implement Predict =================
#  After training the neural network, we would like to use it to predict
#  the labels. You will now implement the "predict" function to use the
#  neural network to predict the labels of the training set. This lets
#  you compute the training set accuracy.

pred = predict(Theta1, Theta2, X)

accuracy = np.mean(np.double(pred == y)) * 100
print('Training Set Accuracy: %f\n'%accuracy)


input("Program paused. Press Enter to exit...")






