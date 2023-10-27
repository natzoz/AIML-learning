import math
import random
import statistics
import matplotlib.pyplot as plt


def f(d):
    return 1 - (0.8**d)


def plot():
    x = range(1, 20)
    y = [f(d) for d in x]

    plt.plot(x, y, label='d')
    plt.show()


def distance(a, b):
    return math.sqrt(sum((ai - bi)**2 for ai, bi in zip(a, b)))


def random_point(d):
    return [random.random() for _ in range(d)]


def avg_dist(d):
    return statistics.mean(distance(random_point(d), random_point(d)) for _ in range(1000000))


for i in range(1, 5):
    print(avg_dist(i))
