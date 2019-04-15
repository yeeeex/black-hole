import numpy as np
import scipy.io as sio
from displayData import*
from predict import*

input_layer_size=400
hidden_layer_size=25
num_labels=10

print('Loading and Visualizing Data ...')
data=sio.loadmat('ex3data1.mat')
X=data['X']
y=data['y'].flatten()
m=X.shape[0]
rand_indices = np.random.permutation(range(m))
rX=X[rand_indices[0:100],:]

displayData(rX)

input('Program paused. Press enter to continue.')

print('\nLoading Saved Neural Network Parameters ...')
weights=sio.loadmat("ex3weights.mat")

Theta1=weights['Theta1']
Theta2=weights['Theta2']

pred=predict(Theta1,Theta2,X)
np.set_printoptions(threshold = np.inf)
np.set_printoptions(suppress=True)
print(pred)
print(y)
print('Training set accuracy: {}'.format(np.mean(pred == y)*100))