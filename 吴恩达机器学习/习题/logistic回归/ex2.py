import numpy as np
import scipy.optimize as opt
from plotData import *
from costFunction import *
from plotDecisionBoundary import *
from sigmoid import *
from predict import *
from costFunctionReg import *

data=np.loadtxt("ex2data1.txt",dtype=np.float64,delimiter=',')

X=data[:,0:2]
y=data[:,2]

# ==================== Part 1: Plotting ====================
#  We start the exercise by first plotting the data to understand the 
#  the problem we are working with.
print('Plotting data with + indicating (y = 1) examples and o indicating (y = 0) examples.')

plotData(X,y)


plt.axis([30, 100, 30, 100])  
plt.legend(['Admitted', 'Not admitted'], loc=1)  
plt.xlabel('Exam 1 score')   
plt.ylabel('Exam 2 score')
plt.show()


# ============ Part 2: Compute Cost and Gradient ============
#  In this part of the exercise, you will implement the cost and gradient
#  for logistic regression. You neeed to complete the code in 
#  costFunction.m
#  Setup the data matrix appropriately, and add ones for the intercept term


(m,n)=X.shape

X=np.c_[np.ones(m),X]
initial_theta=np.zeros(n+1)

cost, grad = costFunction(initial_theta, X, y)

print('Cost at initial theta (zeros): %f'%cost)
print('Expected cost (approx): 0.693')
print('Gradient at initial theta (zeros): ')
print("gard:")
print(grad)
print('Expected gradients (approx): -0.1000 -12.0092 -11.2628')


# Compute and display cost and gradient with non-zero theta
test_theta = np.array([-24, 0.2, 0.2])
test_theta.reshape(3,1)
[cost, grad] = costFunction(test_theta, X, y)

print('Cost at test theta: %f', cost)
print('Expected cost (approx): 0.218')
print('Gradient at test theta: ')
print("grad:")
print(grad)
print('Expected gradients (approx): 0.043 2.566 2.647')

input('Program paused. Press enter to continue.')


# ============= Part 3: Optimizing using fminunc  =============
#  In this exercise, you will use a built-in function (fminunc) to find the
#  optimal parameters theta.
def cost_func(t):  #单独写一个计算代价的函数  返回代价函数值
    return costFunction(t, X, y)[0]


def grad_func(t): #单独写一个计算梯度的函数 返回梯度值
    return costFunction(t, X, y)[1]


# 运行高级优化方法
theta, cost, *unused = opt.fmin_bfgs(f=cost_func, fprime=grad_func, x0=initial_theta, maxiter=400, full_output=True, disp=False)

print('Cost at theta found by fmin: {:0.4f}'.format(cost))
print('Expected cost (approx): 0.203')
print('theta: \n{}'.format(theta))
print('Expected Theta (approx): \n-25.161\n0.206\n0.201')

# 画出决策边界
plot_decision_boundary(theta, X, y)

plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')

plt.show()
input('Program paused. Press ENTER to continue')

# ============== Part 4: Predict and Accuracies ==============
#  After learning the parameters, you will like to use it to predict the outcomes
# on unseen data. In this part, you will use the logistic regression model
#  to predict the probability that a student with score 45 on exam 1 and 
#  score 85 on exam 2 will be admitted.
#
#  Furthermore, you will compute the training and test set accuracies of 
#  our model.
#
#  Your task is to complete the code in predict.m
#  Predict probability for a student with score 45 on exam 1 
#  and score 85 on exam 2 

exam=np.array([1,45,85])
print(theta)
prob=h(exam,theta)
print('test prob:')
print('For a student with scores 45 and 85, we predict an admission probability of {:0.4f}'.format(prob))
print('Expected value: 0.775 +/- 0.002\n\n')

# Compute accuracy on our training set
p = predict(theta, X)

print('Train accuracy: {}'.format(np.mean(y == p) * 100))
print('Expected accuracy (approx): 89.0\n')
print('\n')

#---------------------regularized logistic regression practices---------------------------
#我将ex2_reg得练习直接接着写了
print("--------strat reg...")
regdata=np.loadtxt("ex2data2.txt",delimiter=',')
regX=regdata[:,0:2]
regy=regdata[:,2]

plotData(regX,regy)

plt.xlabel('Microchip Test 1')
plt.ylabel('Microchip Test 2')
plt.show()


# =========== Part 1: Regularized Logistic Regression ============
#  In this part, you are given a dataset with data points that are not
#  linearly separable. However, you would still like to use logistic
#  regression to classify the data points.
#
#  To do so, you introduce more features to use -- in particular, you add
#  polynomial features to our data matrix (similar to polynomial
#  regression).
#
# Add Polynomial Features
# Note that mapFeature also adds a column of ones for us, so the intercept
# term is handled
print("test map_before:")
print(regX)
regX = map_feature(regX[:,0], regX[:,1])
print("test map_after:")
print(regX)
i_theta=np.zeros(regX.shape[1])
reglambda=1
J,grad=costfunction_reg(i_theta,regX,regy,reglambda)
np.set_printoptions(formatter={'float': '{: 0.4f}\n'.format})
print('Cost at initial theta (zeros): %f'%J)
print('Expected cost (approx): 0.693\n')
print('Gradient at initial theta (zeros) - first five values only:\n')
print(' %f \n', grad[0:5])
print('Expected gradients (approx) - first five values only:\n')
print(' 0.0085\n 0.0188\n 0.0001\n 0.0503\n 0.0115\n')

print('\nProgram paused. Press enter to continue.\n')

test_theta = np.ones(regX.shape[1])
cost, grad= costfunction_reg(test_theta, regX, regy, 10)

print('\nCost at test theta (with lambda = 10): %f'%cost)
print('Expected cost (approx): 3.16')
print('Gradient at test theta - first five values only:')
print(grad[0:5])
print('Expected gradients (approx) - first five values only:')
print(' 0.3460\n 0.1614\n 0.1948\n 0.2269\n 0.0922')
print('\nProgram paused. Press enter to continue.')




# ============= Part 2: Regularization and Accuracies =============
#  Optional Exercise:
#  In this part, you will get to try different values of lambda and
#  see how regularization affects the decision coundart
#
#  Try the following values of lambda (0, 1, 10, 100).
#
#  How does the decision boundary change when you vary lambda? How does
#  the training set accuracy vary?

i2_theta=np.zeros(regX.shape[1])
reglambda=1
def costf(t):
    return costfunction_reg(t,regX,regy,reglambda)[0]

def gradf(t):
    return costfunction_reg(t, regX, regy,reglambda)[1]

i2_theta, cost, *unused = opt.fmin_bfgs(f=costf, fprime=gradf, x0=i2_theta, maxiter=400, full_output=True, disp=False)

print('Plotting decision boundary ...')
plot_decision_boundary(i2_theta, regX, regy)
plt.title('lambda = {}'.format(reglambda))

plt.xlabel('Microchip Test 1')
plt.ylabel('Microchip Test 2')
plt.show()
p=predict(i2_theta,regX)

print('Train Accuracy: {:0.4f}'.format(np.mean(regy == p) * 100))
print('Expected accuracy (with lambda = 1): 83.1 (approx)')

input('ex2_reg Finished. Press ENTER to exit')


