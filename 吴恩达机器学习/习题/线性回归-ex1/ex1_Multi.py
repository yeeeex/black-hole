import matplotlib.pyplot as plt
import numpy as np
from featureNormalize import *
from gradientDescent import *
from normalEqn import *
from computeCostMulti import *

plt.ion()
print('loading data...')
np.set_printoptions(suppress=True)#浮点输出，而非科学计数法
data=np.loadtxt('ex1data2.txt',delimiter=',',dtype=np.float,comments='#')
x=data[:,0:2]
y=data[:,2]
#test start
print('----test [:,0]----')
print(x)
# [:,0]表示取特定列的全部，[0,:]表示取特定行的全部

print("------test [0,:]----")
print(y)
#test end

m=y.size
print('First 10 examples from the dataset:')
for i in range(0,10):
    print('%d %d %d'%(x[i,0],x[i,1],y[i]))

input('Program paused. Press enter to continue.\n')

print('Normalizing Features ...')
#normalizing是指数据缩放
x,mu,sigma=featureNormalize(x)
x = np.c_[np.ones(m), x]
theta=np.zeros(x.shape[1])

alpha = 0.03
num_iters = 400

theta,j_history=gradientDescentMulti(x,y,theta,alpha,num_iters)
print("------test j_history-------")
print(j_history)

# 绘制代价函数值随迭代次数的变化曲线
plt.figure()

plt.plot(np.arange(j_history.size), j_history)
plt.xlabel('Number of iterations')
plt.ylabel('Cost J')
plt.show()
# 打印求解的最优的参数
print('Theta computed from gradient descent : \n{}'.format(theta))

# 预测面积是1650 卧室数是3 的房子的价格

x1=np.array([1650,3])

x1=(x1-mu)/sigma  #对预测样例进行特征缩放
x1=np.r_[1,x1]  #前面增加一个1
price = h(x1,theta)  #带入假设函数 求解预测值


# ==========================================================

print('Predicted price of a 1650 sq-ft, 3 br house (using gradient descent) : {:0.3f}'.format(price))


input('Program paused. Press ENTER to continue')

#use normal equations to solve

print('Solving with normal equations...')

newdata=np.loadtxt('ex1data2.txt',delimiter=',',dtype=np.float,comments='#')
x = data[:, 0:2]
y = data[:, 2]
m = y.size

# 增加一列特征1
x = np.c_[np.ones(m), x]

theta=normal_eqn(x,y)

print(theta)

