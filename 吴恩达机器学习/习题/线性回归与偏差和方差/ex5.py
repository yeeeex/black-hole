import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from linearRegCostFunction import *
from trainLearnReg import *
from learningCurve import*
from plotFeatures import*
from featureNormalize import*
from plotFit import*
from validationCurve import *
print('Loading and Visualizing Data ...')
data=sio.loadmat('ex5data1.mat')
X=data['X']
y=data['y']
Xval=data['Xval']
yval=data['yval']
Xtest=data['Xtest']
ytest=data['ytest']
plt.xlabel('Change in water level (x)')
plt.ylabel('Water flowing out of the dam (y)')
plt.scatter(X,y,c='red',marker='x',linewidths=10)
plt.show()
input('Program paused. Press enter to continue.\n')
m=X.shape[0]
theta=np.array([1,1])
J=linearRegCostFunction(np.c_[np.ones((X.shape[0],1)),X],y,theta,1)[0]

print('Cost at theta = [1 ; 1]: %f \n(this value should be about 303.993192)'%J)


input('Program paused. Press enter to continue.\n')


# =========== Part 3: Regularized Linear Regression Gradient =============
#  You should now implement the gradient for regularized linear 
#  regression.
#
theta =np.array([1,1])
J,grad=linearRegCostFunction(np.c_[np.ones((X.shape[0],1)),X],y,theta,1)
print(grad.shape)


print('Gradient at theta = [1 ; 1]:  [%f; %f] \
    \n(this value should be about [-15.303016; 598.250744])\n')
print(grad)



input('Program paused. Press enter to continue.\n')

# =========== Part 4: Train Linear Regression =============
#  Once you have implemented the cost and gradient correctly, the
#  trainLinearReg function will use your cost function to train 
#  regularized linear regression.
#  Write Up Note: The data is non-linear, so this will not give a great 
#  fit.

lmd=0
theta_result=trainLinearReg(np.c_[np.ones((X.shape[0],1)),X],y,lmd)
print(theta_result)
Xnew=np.c_[np.ones((X.shape[0],1)),X]
plt.xlabel('Change in water level (x)')
plt.ylabel('Water flowing out of the dam (y)')
plt.scatter(X,y,c='red',marker='x',linewidths=10)
plt.plot(X,Xnew.dot(theta_result.T))
plt.show()

input('Program paused. Press enter to continue.\n')
    # =========== Part 5: Learning Curve for Linear Regression =============
#  Next, you should implement the learningCurve function. 
#
#  Write Up Note: Since the model is underfitting the data, we expect to
#                 see a graph with "high bias" -- Figure 3 in ex5.pdf 

lmd=0

error_train,error_val=learningCurve(np.c_[np.ones((X.shape[0],1)),X],y,np.c_[np.ones((Xval.shape[0],1)),Xval],yval,lmd)
plt.figure()
plt.plot(np.arange(m),error_train)
plt.plot(np.arange(m), error_val)
plt.title('Learning Curve for Linear Regression')
plt.legend(['Train', 'Cross Validation'])
plt.xlabel('Number of Training Examples')
plt.ylabel('Error')
plt.axis([0, 13, 0, 150])
plt.show()

print('# Training Examples\tTrain Error\tCross Validation Error')
for i in range(m):
    print(' \t%d'%i,end='')
    print(' \t%d'%error_train[i],end='')
    print(' \t%d'%error_val[i],end='')

input('Program paused. Press enter to continue.\n')

# =========== Part 6: Feature Mapping for Polynomial Regression =============
#  One solution to this is to use polynomial regression. You should now
#  complete polyFeatures to map each example into its powers
#
p = 8
X_poly=polyFeatures(X,p)
X_poly, mu, sigma = featureNormalize(X_poly)
X_poly = np.c_[np.ones((m, 1)), X_poly]

X_poly_test = polyFeatures(Xtest, p)
X_poly_test-=mu
X_poly_test/=sigma
X_poly_test = np.c_[np.ones((ytest.shape[0], 1)), X_poly_test]

X_poly_val = polyFeatures(Xval, p)
X_poly_val-=mu
X_poly_val/=sigma
X_poly_val = np.c_[np.ones((yval.shape[0], 1)), X_poly_val]

print('Normalized Training Example 1 : \n{}'.format(X_poly[0]))

# =========== Part 7: Learning Curve for Polynomial Regression =============
#  Now, you will get to experiment with polynomial regression with multiple
#  values of lambda. The code below runs polynomial regression with 
#  lambda = 0. You should try running the code with different values of
#  lambda to see how the fit and learning curve change.

lmd=1
np.set_printoptions(suppress=True)
print(X_poly)
theta=trainLinearReg(X_poly,y,lmd)
print(theta)
X_fit,y_fit=plotFit(np.min(X),np.max(X),mu,sigma,theta,p)
plt.scatter(X,y,c='r',marker='x')
plt.plot(X_fit,y_fit)
plt.xlabel('Change in water level (x)')
plt.ylabel('Water folowing out of the dam (y)')
plt.ylim([-60, 60])
plt.title('Polynomial Regression Fit (lambda = {})'.format(lmd))
plt.show()

error_train, error_val = learningCurve(X_poly, y, X_poly_val, yval, lmd)
plt.figure(4)
plt.plot(np.arange(m), error_train, np.arange(m), error_val)
plt.title('Polynomial Regression Learning Curve (lambda = {})'.format(lmd))
plt.legend(['Train', 'Cross Validation'])
plt.xlabel('Number of Training Examples')
plt.ylabel('Error')
plt.axis([0, 13, 0, 150])
plt.show()
print('Polynomial Regression (lambda = {})'.format(lmd))
print('# Training Examples\tTrain Error\t\tCross Validation Error')
for i in range(m):
    print('  \t{}\t\t{}\t{}'.format(i, error_train[i], error_val[i]))

lambda_vec ,error_train,error_val=validationCurve(X_poly,y,X_poly_val,yval)
plt.plot(lambda_vec,error_train)
plt.plot(lambda_vec,error_val)
plt.xlabel('lambda')
plt.ylabel('Error')
plt.show()
