import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def Vector_distance(u, v):
    diff = (u - v)
    return diff.dot(diff)

def cluster(X, K, Max_Operations=20, beta=3.0, show_plots=False):
    N, D = X.shape
    exponents = np.empty((N, K))

    initial_centers = np.random.choice(N, K, replace=False)

    M = X[initial_centers]

    k = 0
    for i in range(Max_Operations):
        k += 1
        for k in range(K):
            for n in range(N):
                exponents[n,k] = np.exp(-beta * Vector_distance(M[k], X[n]))
        R = exponents / exponents.sum(axis=1, keepdims=True)

        for k in range(K):
            M[k] = R[:,k].dot(X) / R[:,k].sum()
        oldM = M

        M = R.T.dot(X) / R.sum(axis=0, keepdims=True).T


    if show_plots:
        random_colors = np.random.random((K, 3))
        colors = R.dot(random_colors)
        plt.scatter(X[:, 0], X[:, 1], c=colors)
        plt.show()

    return M, R



def main():
    iris = pd.read_csv("iris.csv")
    print(iris)
    w = iris.values[:, 0:1]
    s = iris.values[:, 2:3]
    z = iris.values[:, 1:2]
    t = iris.values[:, 3:4]

    w = np.array(w)
    s = np.array(s)
    z = np.array(z)
    t = np.array(t)

    x = w + s
    y = z + t

    plt.scatter(x[:,0], y[:,0])
    plt.show()

    print("--------")
    x = np.column_stack((x, y))
    print(x)


    сluster_count = 3
    cluster(x, сluster_count, Max_Operations= 40, show_plots=True)
    сluster_count = 2
    cluster(x, сluster_count, Max_Operations= 40, show_plots=True)



if __name__ == '__main__':
    main()