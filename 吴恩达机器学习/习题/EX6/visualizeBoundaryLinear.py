import numpy as np
from plotData import *
import matplotlib.pyplot as plt
def visualizeBoundaryLinear(X, y, model):
    w=model.coef_.flatten()
    b=model.intercept_.flatten()
    xp=np.linspace(min(X[:,0]),max(X[:,0]),100)
    yp = -(w[0]*xp + b)/w[1]
    plotData(X, y)

    plt.plot(xp, yp, '-b')
    plt.show()
