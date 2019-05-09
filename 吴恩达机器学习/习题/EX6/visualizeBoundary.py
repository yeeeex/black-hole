from plotData import*

def visualizeBoundary_old(clf,X, y, model):
    plotData(X, y)
    plt.show()
    # Make classification predictions over a grid of values
    x1plot = np.linspace(min(X[:,0]), max(X[:,0]), X.shape[0]).T
    x2plot = np.linspace(min(X[:,1]), max(X[:,1]), X.shape[0]).T
    X1, X2 = np.meshgrid(x1plot, x2plot)
    vals = np.zeros(X1.shape)

    for i in range(X1.shape[1]):
        this_X = np.c_[X1[:, i], X2[:, i]]
        vals[:, i] = clf.predict(this_X)

    # Plot the SVM boundary
    #contour(X1, X2, vals, [0 0], 'Color', 'b')
    plt.contour(X1, X2, vals, levels=[0.0, 0.0])
    plt.show()

