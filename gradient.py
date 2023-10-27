import matplotlib.pyplot as plt
import numpy as np
import random
import math


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


def random_restart(search, f):
    best = search(f)
    for i in range(20):
        attempt = search(f)
        if attempt < best:
            best = attempt
    return best


def gradient_descent_2d(f):
    epsilon = 0.001
    learning_rate = 0.0001
    x = random.random()
    y = random.random()
    iterations = 0

    while True:
        x1 = x + epsilon
        y1 = y + epsilon

        z = f(x, y)
        z1 = f(x, y1)
        z2 = f(x1, y)

        gradient_x = (z2 - z) / (x1 - x)
        gradient_y = (z1 - z) / (y1 - y)

        gradient_vector = math.sqrt((gradient_x**2) + (gradient_y**2))

        if abs(gradient_vector) < epsilon:
            # print(f'That took {iterations} iterations')
            return x, y

        x -= learning_rate * gradient_x
        y -= learning_rate * gradient_y
        iterations += 1


print(gradient_descent_2d(f3))
print(random_restart(gradient_descent_2d, f4))
