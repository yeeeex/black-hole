import numpy as np
import scipy.io as sio
from findClosestCentroids import*
from computeCentroids import*
from runkMeans import*
from kMeansInitCentroids import*
print('Finding closest centroids.\n')

data=sio.loadmat("ex7data2.mat")
X=data['X']

K=3
#初始有3个 cluster中心
init_centroids=np.array([3,3,6,2,8,5]).reshape((3,2))#初始的中心点

idx=findClosestCentroids(X,init_centroids)

print('Closest centroids for the first 3 examples: ')
print(idx[0:3])
print('\n(the closest centroids should be 1, 3, 2 respectively)')

input('Program paused. Press enter to continue.')

# ===================== Part 2: Compute Means =========================
#  After implementing the closest centroids function, you should now
#  complete the computeCentroids function.

print('\nComputing centroids means.\n')
#Compute means based on the closest centroids found in the previous part.
centroids = computeCentroids(X, idx, K)

print('Centroids computed after initial finding of closest centroids: ')
print(centroids)
print('\n(the centroids should be')
print('   [ 2.428301 3.157924 ]')
print('   [ 5.813503 2.633656 ]')
print('   [ 7.119387 3.616684 ]\n')

input('Program paused. Press enter to continue.\n')

# =================== Part 3: K-Means Clustering ======================
#  After you have completed the two functions computeCentroids and
#  findClosestCentroids, you have all the necessary pieces to run the
#  kMeans algorithm. In this part, you will run the K-Means algorithm on
#  the example dataset we have provided. 
#

print('\nRunning K-Means clustering on example dataset.\n')
sio.loadmat('ex7data2.mat')

K=3
max_iters=10

initial_centroids =np.array([3 ,3,6 ,2,8 ,5]).reshape((3,2))
centroids, idx = runkMeans(X, initial_centroids, max_iters, True)

print('\nK-Means Done.\n')

input('Program paused. Press enter to continue.\n')

#============= Part 4: K-Means Clustering on Pixels ===============
#  In this exercise, you will use K-Means to compress an image. To do this,
#  you will first run K-Means on the colors of the pixels in the image and
#  then you will map each pixel onto its closest centroid.
#  
#  You should now complete the code in kMeansInitCentroids.m
#

data=sio.loadmat('bird_small.mat')
A=data['A']
A=A/255
print(A.shape)
(img_m,img_n,img_l)=A.shape
X = A.reshape(img_m * img_n, 3)

K=16

max_iters=10
initial_centroids =kMeansInitCentroids(X, K)

centroids, idx = runkMeans(X, initial_centroids, max_iters)

print('Program paused. Press enter to continue.\n')

# ================= Part 5: Image Compression ======================
#  In this part of the exercise, you will use the clusters of K-Means to
#  compress an image. To do this, we first find the closest clusters for
#  each example. After that, we 

print('\nApplying K-Means to compress an image.\n')

idx = findClosestCentroids(X, centroids).astype(int)
X_recovered = centroids[idx]
X_recovered=X_recovered.reshape(img_m,img_n,3)

plt.subplot(1, 2, 1)
plt.imshow(A)
plt.title('Original')
plt.show()


plt.subplot(1, 2, 2)
plt.imshow(X_recovered)
plt.title('Compressed, with %d colors.' %K)
plt.show()

input("Program paused. Press Enter to continue...")



