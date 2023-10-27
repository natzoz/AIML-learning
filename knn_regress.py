import math
import random
from statistics import mean
import matplotlib.pyplot as plt


class Point:
    def __init__(self, coords, f):
        if type(coords) == int:  # Number of coordinates specified
            self.coords = [random.random() for _ in range(coords)]
        else:  # Sequence of coordinates specified
            self.coords = coords
        self.target = f(self.coords)

    def __str__(self):
        return f'{self.coords} -> {self.target}'

    def __repr__(self):
        return str(self)

    def distance_to(self, other):
        squared_differences = [(a-b)**2 for a, b in zip(self.coords, other.coords)]
        return math.sqrt(sum(squared_differences))


def f3(coords):
    x, y = coords
    r = math.sqrt(((x-0.3)*3)**2 + ((y-0.6)*3)**2)
    return (-math.sin(r) / r) + random.gauss(0, 0.1)


def f4(coords):
    x, y = coords
    def g(x1, y1, sigma):
        return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(1 / (2 * sigma**2)) * ((x-x1)**2 + (y-y1)**2))
    return (-(g(0.1, 0.1, 0.1) + g(0.6, 0.7, 0.2) + g(0.5, 0.2, 0.12))) + random.gauss(0, 0.1)


def knn_regress(k, train, p):
    '''
    :param k: The number of neighbors to consider.
    :param train: A sequence of Points.
    :param p: The point whose target is to be predicted.
    :return: The k-nearest-neighbors prediction for the target of p.
    '''
    nearest = sorted(train, key=p.distance_to)[:k]
    winner = mean(p.target for p in nearest)
    return winner


def mse(k, train, test):
    error = ((knn_regress(k, train, p) - p.target)**2 for p in test)
    return mean(error)


# Put your plotting code here
trainf3 = [Point(2, f3) for _ in range(500)]
testf3 = [Point(2, f3) for _ in range(500)]

trainf4 = [Point(2, f4) for _ in range(500)]
testf4 = [Point(2, f4) for _ in range(500)]

train_mse_f3 = [mse(k, trainf3, trainf3) for k in range(1, 49, 2)]
test_mse_f3 = [mse(k, trainf3, testf3) for k in range(1, 49, 2)]

train_mse_f4 = [mse(k, trainf4, trainf4) for k in range(1, 49, 2)]
test_mse_f4 = [mse(k, trainf4, testf4) for k in range(1, 49, 2)]

plt.plot(train_mse_f3, label='Training set f3')
plt.plot(test_mse_f3, label='Test set f3')
plt.xlabel('k')
plt.ylabel('mse')
plt.legend()
plt.show()

plt.plot(train_mse_f4, label='Training set f4')
plt.plot(test_mse_f4, label='Test set f4')
plt.xlabel('k')
plt.ylabel('mse')
plt.legend()
plt.show()

# Put your answers to the questions here
'''
f3:
For the training set, what is the best value of k?
1
Is it important that we use exactly this value, or is it sufficient to be somewhere close to it?
It's important that we use exactly this value.
For the testing set, what is the best value of k?
6
Is it important that we use exactly this value, or is it sufficient to be somewhere close to it?
It's sufficient to be somewhere close to it.

f4:
For the training set, what is the best value of k?
1
Is it important that we use exactly this value, or is it sufficient to be somewhere close to it?
It's important that we use exactly this value.
For the testing set, what is the best value of k?
1
Is it important that we use exactly this value, or is it sufficient to be somewhere close to it?
It's important that we use exactly this value.
'''
