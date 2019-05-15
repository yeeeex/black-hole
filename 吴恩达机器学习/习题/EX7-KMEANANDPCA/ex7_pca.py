import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from featureNormalize import*
from pca import*
from runkMeans import*
from projectData import*
from recoverData import*
from displayData import*
from kMeansInitCentroids import*
print('Visualizing example dataset for PCA.\n')

data=sio.loadmat('ex7data1.mat')
X=data['X']
plt.scatter(X[:,0],X[:,1])
plt.axis([0.5,6.5,2,8])
plt.show()
input('Program paused. Press enter to continue.\n')

# =============== Part 2: Principal Component Analysis ===============
#  You should now implement PCA, a dimension reduction technique. You
#  should complete the code in pca.m
#
print('\nRunning PCA on example dataset.\n')

X_norm,mu,sigma=featureNormalize(X)

U,S=pca(X_norm)
print(X_norm.shape)
print(mu.shape)
print(sigma.shape)
print(U.shape)
print(S.shape)
drawLine(mu, mu + 1.5 * S[0] * U[:, 0])
drawLine(mu, mu + 1.5 * S[1] * U[:, 1])
plt.scatter(X[:,0],X[:,1])
plt.axis([0.5,6.5,2,8])
plt.show()
print('Top eigenvector: \nU[:, 0] = {}'.format(U[:, 0]))
print('You should expect to see [-0.707107 -0.707107]')

input('Program paused. Press ENTER to continue')


# =================== Part 3: Dimension Reduction ===================
#  You should now implement the projection step to map the data onto the 
#  first k eigenvectors. The code will then plot the data in this reduced 
#  dimensional space.  This will show you what the data looks like when 
#  using only the corresponding eigenvectors to reconstruct it.
#
#  You should complete the code in projectData.m
#
print('\nDimension reduction on example dataset.\n')
plt.plot(X_norm[:,0], X_norm[:,1])
plt.axis([-4,3,-4,3])# axis square
K=1
Z=projectData(X_norm,U,K)
print('Projection of the first example: %f\n'%Z[0,:])
print('\n(this value should be about 1.481274)\n')

X_rec  = recoverData(Z, U, K)
print('Approximation of the first example: %f %f'%(X_rec[0,0], X_rec[0,1]))
print('\n(this value should be about  -1.047419 -1.047419)\n')


plt.scatter(X_rec[:,0], X_rec[:,1],facecolors='none', edgecolors='r', s=20)
for i in range(X_norm.shape[0]):
    drawLine(X_norm[i], X_rec[i])
plt.show()
input('Program paused. Press enter to continue.\n')

# =============== Part 4: Loading and Visualizing Face Data =============
#  We start the exercise by first loading and visualizing the dataset.
#  The following code will load the dataset into your environment
#
print('\nLoading face dataset.\n')

data=sio.loadmat('ex7faces.mat')
X=data['X']
display_data(X[0:100,:])

input('Program paused. Press enter to continue.\n')


# =========== Part 5: PCA on Face Data: Eigenfaces  ===================
#  Run PCA and visualize the eigenvectors which are in this case eigenfaces
#  We display the first 36 eigenfaces.

print('\nRunning PCA on face dataset.\n\
         (this might take a minute or two ...)\n\n')

#  Before running PCA, it is important to first normalize X by subtracting 
#  the mean value from each feature

X_norm,mu,sigma=featureNormalize(X)
U,S=pca(X_norm)

display_data(U[:,0:36])

input('Program paused. Press enter to continue.')


# ============= Part 6: Dimension Reduction for Faces =================
#  Project images to the eigen space using the top k eigenvectors 
#  If you are applying a machine learning algorithm 
print('\nDimension reduction for face dataset.\n')

K = 100
Z = projectData(X_norm, U, K)

print('The projected data Z has a size of:')
print(Z.shape)

input('\n\nProgram paused. Press enter to continue.')

# ==== Part 7: Visualization of Faces after PCA Dimension Reduction ====
#  Project images to the eigen space using the top K eigen vectors and 
#  visualize only using those K dimensions
#  Compare to the original input, which is also displayed

print('\nVisualizing the projected (reduced dimension) faces.\n')

K = 100
X_rec  = recoverData(Z, U, K)

display_data(X_norm[0:100])
plt.title('Original faces')
display_data(X_rec[0:100])

input('Program paused. Press ENTER to continue')


# === Part 8(a): Optional (ungraded) Exercise: PCA for Visualization ===
#  One useful application of PCA is to use it to visualize high-dimensional
#  data. In the last K-Means exercise you ran K-Means on 3-dimensional 
#  pixel colors of an image. We first visualize this output in 3D, and then
#  apply PCA to obtain a visualization in 2D.

data=sio.loadmat('bird_small.mat')
X=data['A']

img_shape=X.shape

X=X.reshape((img_shape[0]*img_shape[1],3))
K=16
max_iters=10
initial_centroids = kMeansInitCentroids(X, K)
centroids, idx = runkMeans(X, initial_centroids, max_iters)
selected = np.random.randint(X.shape[0], size=1000)



input('Program paused. Press ENTER to continue')

# ===================== Part 8(b): PCA for Visualization =====================
# Use PCA to project this cloud to 2D for visualization

X_norm, mu, sigma = featureNormalize(X)

# PCA and project the data to 2D
U, S = pca(X_norm)
Z = projectData(X_norm, U, 2)

# Plot in 2D

plt.scatter(Z[selected, 0], Z[selected, 1], c=idx[selected].astype(np.float64), s=15)
plt.title('Pixel dataset plotted in 2D, using PCA for dimensionality reduction')
plt.figure()
input('ex7_pca Finished. Press ENTER to exit')



