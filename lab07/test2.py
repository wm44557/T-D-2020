import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
from matplotlib import pyplot as plt
from scipy.spatial.distance import cdist
from scipy.spatial import distance
import numpy as np
from scipy.spatial.distance import mahalanobis
import math
import scipy

# ----------->Odległośc Euklidesowa między 2 punktami
X = [[0.0, 0.0, 0.0, 152.0, 12.29], [
    0.0, 0.0, 0.357, 245.0, 10.4], [0.0, 0.0, 0.10, 200.0, 11.0]]

C = [[0.0, 0.0, 0.0, 72.0, 12.9], [0.0, 0.0, 0.0, 80.0, 11.3]]


def funkcja(list1, list2):
    squares = [(p-q) ** 2 for p, q in zip(list1, list2)]
    return sum(squares) ** .5


d2 = []
for i in C:
    foo = [funkcja(i, j) for j in X]
    d2.append(foo)

print(d2)


# -----------> Odległość Mahalnobisa
# Średnia
M = [10, 7]
# Kowariancja
V = np.array([[9, -2],
              [-2,  2]])

x = np.random.multivariate_normal(M, V, size=3)
# Obliczyć dystans Mahalanobisa dla każdego punktu w próbce.
mdist = cdist(x, [M], metric='mahalanobis', V=V)[:, 0]

print(mdist)


def distp(X, C):
    de = []
    for i, Ci in enumerate(C):
        de.append(np.sqrt((X-Ci).dot(np.transpose(X-Ci))))
    return de


def single_distp(X, C):
    return np.sqrt((X-C).dot(np.transpose(X-C)))


def distm(X, C, V):
    dm = []
    invertedV = np.linalg.inv(V)
    for i, Xi in enumerate(X):
        dm.append([])
        for k, Ck in enumerate(C):
            dm[i].append(np.sqrt((Xi-Ck)*invertedV*np.transpose(Xi-Ck)))
    return dm


def ksrodki(X, k):
    max = np.max(X, axis=0)

    C = np.random.rand(k, X.shape[1])*max
    lastC = np.zeros((k, X.shape[1]))

    s = np.zeros((X.shape[0]))

    iterations = 0
    cl = np.zeros(X.shape[0])
    while iterations < 100 and not np.array_equal(C, lastC):
        iterations += 1
        lastC = np.copy(C)
        for i in range(X.shape[0]):
            s = distp(X[i], C)
            cluster = np.argmin(s)
            cl[i] = cluster
        for i in range(k):
            p = [X[j] for j in range(len(X)) if cl[j] == i]
            C[i] = np.mean(p, axis=0)
        return C, cl


df = pd.read_csv('autos.csv')
X = df[['horsepower', 'price']]
X = X.to_numpy()
X[np.isnan(X)] = 0
print(X)

# X = np.array([[1, 2],
#              [1.5, 1.8],
#              [5, 8 ],
#              [8, 8],
#              [1, 0.6],
#              [2, 4.6],
#              [7, 8.6],
#              [10, 9.6],
#              [9,11]
#              ])

# X=np.random.randint(100,size=(100,2))

k = 2
C, CX = ksrodki(X, k)

for i in range(k):
    points = []
    for j in range(len(X)):
        if CX[j] == i:
            points.append(X[j])
            print(X[j])
    points = np.asarray(points)
    plt.scatter(points[:, 0], points[:, 1], s=20)

plt.scatter(C[:, 0], C[:, 1], marker="x", c='k', s=100)

plt.show()

suma = 0.0
for i in range(len(X)):
    suma += single_distp(X[i], C[int(CX[i])])
print(suma/len(X))
