import numpy as np
import matplotlib.pyplot as plt

# Generate data
a = np.random.randn(200, 2) * np.array([0.1]) + np.array([0.5, 0.3])
b = np.random.randn(200, 2) * np.array([0.1]) + np.array([0.8, 0.7])
c = np.random.randn(200, 2) * np.array([0.1]) + np.array([0.1, 0.9])

data = np.concatenate((a, b, c))

# Choose k, number of clusters
k = 3

# Initial random centroids
rng = np.random.default_rng()
centroids = rng.random((k, 2))

classes = np.zeros(len(data))

# print(data.shape)


def plot(data):
    for i in range(k):
        plt.scatter(data[classes == i, 0], data[classes == i, 1], s=2, label=str(i))            # : -> every row in col 0 and 1
        plt.legend()
    plt.show()

plot(data)

# Main algorithm
while True:
    # Compute distances
    # List of k arrays, distance from every point to each centroid
    d = [np.linalg.norm(data - centroids[i, :], axis=1) for i in range(k)]

    # Transpose, swap rows and columns
    distances = np.array(d).T

    # Make a copy of classes
    old_classes = np.copy(classes)

    # Classify points by nearest centroid
    # Argmin, location of the smallest value, argument to minimize
    classes = np.argmin(distances, axis=1)

    # If classes haven't changed, stop
    if all(classes == old_classes):
        print('Converged!')
        plot(data)
        break

    # Update centroids
    for i in range(k):
        centroids[i, :] = np.mean(data[classes == i], axis=0)

    # Display progress
    print(centroids)
    plot(data)
