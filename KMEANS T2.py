#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(11)

means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis=0)


def initialize_centroids(X, k):
    centroid = X.copy()
    np.random.shuffle(centroid)
    return centroid[: k]

def get_centroid(x, centroid):
    result = np.sqrt((centroid[:, 0] - x[0])**2 + (centroid[:, 1] - x[1])**2)
    res = result.argmin()
    return res

def distance(X, centroid):
    label = np.apply_along_axis(get_centroid, 1, X, centroid)
    return label

def move_centroids1(X, closest, centroids):
    return np.array([X[closest == i].mean(axis=0) for i in range(centroids.shape[0])])


def kmeans(A, oldcentroid):
    while True:
        f = distance(A, oldcentroid)
        newcentroid = move_centroids1(A, f, oldcentroid)
        if np.array_equal(newcentroid, oldcentroid)==True:
            p=newcentroid
            break
        oldcentroid = newcentroid
    return f

def kmeans_display(X, k, label):

    color = ['b','g','r','c','m', 'y', 'k','w']
    unique_label = np.unique(label)
    for i in range(k):
        cluster = X[label == unique_label[i]]
        plt.plot(cluster[:, 0], cluster[:, 1], color[i] + 'o', markersize=4, alpha=.8)
    plt.axis('equal')
    plt.xlim(left = -1, right = 10)
    plt.ylim((-1,10))
    plt.show()

c = initialize_centroids(X, 3)
e = kmeans(X, c)
kmeans_display(X, 3, e)


# In[ ]:




