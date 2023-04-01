#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = ['purple', 'green', 'orange']
label_dict = {0: 'Iris Setosa', 1: 'Iris Versicolor', 2: 'Iris Virginica'}

for i in range(len(labels)):
    label = label_dict[labels[i]]
    color = colors[labels[i]]
    ax.scatter(pca_data[i, 0], pca_data[i, 1], pca_data[i, 2],
               c=color, label=label)

ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')
ax.set_title('PCA of Iris Dataset')
ax.legend()
plt.show()
