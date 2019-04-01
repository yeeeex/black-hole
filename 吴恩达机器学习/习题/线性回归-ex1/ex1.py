import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import axes3d, Axes3D
from computeCost import *
from gradientDescent import *
from plotData import *
from normalEQN import*

'''第1部分 可视化训练集'''
print('Plotting Data...')
data = np.loadtxt('ex1data1.txt', delimiter=',', usecols=(0, 1))#加载txt格式的数据集 每一行以","分隔
print(data)
#loadtxt 会返回 array这个数据结构，data就是个array，对于二维数组不能直接切片，而要对array
#才能如下data[:,0]一样切片
X = data[:, 0]   #输入变量 第一列
y = data[:, 1]   #输出变量 第二列

#test
if y.size==X.size:
        print("x.size=y.size OK")
m = y.size     #样本数

plt.ion()
plt.figure(0)
#need complete
plot_data_self(X, y)  #可视化数据集



input('Program paused. Press ENTER to continue')


'''第2部分 梯度下降法'''
print('Running Gradient Descent...')

X = np.c_[np.ones(m), X]  # 输入特征矩阵 前面增加一列1 方便矩阵运算
#c_的作用是连接两个矩阵，按行连接，r_按列连接
theta = np.zeros(2)  # 初始化两个参数为0  
#如果np.zeros((2,2)) 那么便是初始化2行大小为2的数组


iterations = 1500  #设置梯度下降迭代次数
alpha = 0.01      #设置学习率
#test
print(X)
print("------------first value---------")

#test  normaleqn for single



# do not  exec
# 计算最开始的代价函数值  并与期望值比较 验证程序正确性
print('Initial cost : ' + str(compute_cost_self(X, y, theta)) + ' (This value should be about 32.07)')
#注意,x是当作引用传入的
#所以说初次代价函数，带入的θ参数是(0,0)
#使用梯度下降法求解线性回归 返回最优参数 以及每一步迭代后的代价函数值

#test
print(X)

theta, J_history = gradient_descent_self(X, y, theta, alpha, iterations)


print("theta :is ")
print(theta)

# 在数据集上绘制出拟合的直线
plt.figure(0)

line1, = plt.plot(X[:, 1], np.dot(X, theta), label='Linear Regression')
#need completed func"plot_data"
plot_data(X[:,1], y)  #可视化数据集
plt.legend(handles=[line1])

input('Program paused. Press ENTER to continue')

# 用训练好的参数 预测人口为3.5*1000时 收益为多少  并与期望值比较 验证程序正确性
predict1 = np.dot(np.array([1, 3.5]), theta)
print('For population = 35,000, we predict a profit of {:0.3f} (This value should be about 4519.77)'.format(predict1*10000))
# 用训练好的参数 预测人口为7*1000时 收益为多少  并与期望值比较 验证程序正确性
predict2 = np.dot(np.array([1, 7]), theta)
print('For population = 70,000, we predict a profit of {:0.3f} (This value should be about 45342.45)'.format(predict2*10000))



input('Program paused. Press ENTER to continue')

'''第3部分 可视化代价函数'''
print('Visualizing J(theta0, theta1) ...')

theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)

xs, ys = np.meshgrid(theta0_vals, theta1_vals)
J_vals = np.zeros(xs.shape)

# Fill out J_vals
for i in range(0, theta0_vals.size):
    for j in range(0, theta1_vals.size):
        t = np.array([theta0_vals[i], theta1_vals[j]])
        J_vals[i][j] = compute_cost(X, y, t)

J_vals = np.transpose(J_vals)

fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.plot_surface(xs, ys, J_vals)
plt.xlabel(r'$\theta_0$')
plt.ylabel(r'$\theta_1$')

plt.figure(2)
lvls = np.logspace(-2, 3, 20)
plt.contour(xs, ys, J_vals, levels=lvls, norm=LogNorm())
plt.plot(theta[0], theta[1], c='r', marker="x")

input('ex1 Finished. Press ENTER to exit')
