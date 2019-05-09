import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
from sklearn import svm
from plotData import*
from visualizeBoundary import*
from gaussianKernel import*
from visualizeBoundaryLinear import *
plt.ion()
np.set_printoptions(formatter={'float': '{: 0.6f}'.format})



print('Loading and Visualizing data ... ')


data = sio.loadmat('ex6data1.mat') 
X = data['X']   
y = data['y'].flatten() 

plotData(X, y)

input('Program paused. Press ENTER to continue')




print('Training Linear SVM')


c = 1
#通过C=1000或者等于1使得其考虑是否忽略数据坐标图中的特殊点
clf = svm.SVC(c, kernel='linear', tol=1e-3,max_iter=200)  
model=clf.fit(X, y)  

plotData(X, y)
visualizeBoundaryLinear(X,y,model) 

input('Program paused. Press ENTER to continue')




print('Evaluating the Gaussian Kernel')

x1 = np.array([1, 2, 1])
x2 = np.array([0, 4, -1])
sigma = 2 
sim = gaussianKernel(x1, x2, sigma) 

print('Gaussian kernel between x1 = [1, 2, 1], x2 = [0, 4, -1], sigma = {} : {:0.6f}\n'
      '(for sigma = 2, this value should be about 0.324652'.format(sigma, sim))

input('Program paused. Press ENTER to continue')




print('Loading and Visualizing Data ...')


data = sio.loadmat('ex6data2.mat')
X = data['X'] 
y = data['y'].flatten() 
m = y.size  


plotData(X, y)

input('Program paused. Press ENTER to continue')



print('Training SVM with RFB(Gaussian) Kernel (this may take 1 to 2 minutes) ...')

#参数设置
c = 1
sigma = 0.1
ga=1.0/(2*sigma**2)
#调用自己写的高斯核函数  返回新的特征向量矩阵
def gaussian_kernel(x_1, x_2):
    n1 = x_1.shape[0]
    n2 = x_2.shape[0]
    result = np.zeros((n1, n2))

    for i in range(n1):
        for j in range(n2):
            result[i, j] = gaussianKernel(x_1[i], x_2[j], sigma)

    return result

# 

clf = svm.SVC(c, kernel='rbf', gamma=ga,tol=1e-3,max_iter=200) 
model=clf.fit(X, y)  
print('Training complete!')

plotData(X, y) 
visualizeBoundary_old(clf,X,y,model) 

input('Program paused. Press ENTER to continue')



print('Loading and Visualizing Data ...')


data = sio.loadmat('ex6data3.mat')
X = data['X']
y = data['y'].flatten()
m = y.size


plotData(X, y)

input('Program paused. Press ENTER to continue')

# ===================== Part 7: Visualizing Dataset 3 =====================

clf = svm.SVC(c, kernel='rbf', gamma=ga,tol=1e-3,max_iter=200)
model=clf.fit(X, y)
print(clf)
plotData(X, y)
visualizeBoundary_old(clf,X,y,model)

input('ex6 Finished. Press ENTER to exit')


 
