import matplotlib.pyplot as plt
import numpy as np
import random
import math


def f1(x):
    return (x-0.73)**2


def f2(x):
    return x - math.sin(1/(x + 0.1))


def plot(f):
    xs = np.linspace(0, 1, 1000)
    ys = [f(x) for x in xs]
    plt.plot(xs, ys)
    plt.show()


# plot(f1)
# plot(f2)


def mc_search(f):
    best_x = 0
    best_y = f(0)
    for i in range(10):  # Try turning this up to 100 or 1000
        x = random.random()
        y = f(x)
        if y < best_y:
            best_x = x
            best_y = y
    return best_x


# print(mc_search(f1))


def grid_search(f):
    best_x = 0
    best_y = f(0)
    xs = np.linspace(0, 1, 10)  # Try turning this up to 100 or 1000
    for x in xs:
        y = f(x)
        if y < best_y:
            best_x = x
            best_y = y
    return best_x


# print(grid_search(f1))


# Pick a point and plot downhill until we hit a valley
def gradient_descent_search(f):
    epsilon = 0.001
    learning_rate = 0.0001
    # learning_rate = 0.0001
    x = random.random()
    iterations = 0
    while True:
        # Compute approximated gradient
        x1 = x + epsilon
        y = f(x)
        y1 = f(x1)
        gradient = (y1 - y) / (x1 - x)
        # print(f'The gradient at {x} is {gradient}')
        # Time to stop?
        if abs(gradient) < epsilon:
            # print(f'That took {iterations} iterations')
            return x
        # Take a step
        x -= learning_rate * gradient
        # print(x)
        iterations += 1


# print(gradient_descent_search(f1))
# print(gradient_descent_search(f2))


def random_restart(search, f):
    best = search(f)
    for i in range(20):
        attempt = search(f)
        if attempt < best:
            best = attempt
        print(best)
    return best


# print(random_restart(gradient_descent_search, f2))


def f3(x, y):
    r = math.sqrt(((x-0.3)*3)**2 + ((y-0.6)*3)**2)
    return -math.sin(r) / r


def f4(x, y):
    def g(x1, y1, sigma):
        return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(1 / (2 * sigma**2)) * ((x-x1)**2 + (y-y1)**2))
    return -(g(0.1, 0.1, 0.1) + g(0.6, 0.7, 0.2) + g(0.5, 0.2, 0.12))


def plot_wireframe(f, contour_height):
    pts = np.linspace(0, 1, 50)
    xs, ys = np.meshgrid(pts, pts)
    zs = np.copy(xs)  # Making it the correct shape
    # This isn't the normal numpy way of doing things, but I wanted to avoid
    # introducing too much new machinery
    for i in range(len(pts)):
        y = pts[i]
        for j in range(len(pts)):
            x = pts[j]
            zs[i, j] = f(x, y)
    _, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.plot_wireframe(xs, ys, zs)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.contour(xs, ys, zs, offset=contour_height)
    plt.show()


# plot_wireframe(f3, -1)
# plot_wireframe(f4, -4)


