import random
import math

LEARNING_RATE = 0.1


class InputNeuron:

    def __init__(self, activation = 1):
        self.activation = activation


class Neuron:

    def __init__(self, previous_layer):
        self.activation = None
        self.previous_layer = [InputNeuron()] + previous_layer             # Neuron that the current neuron is connected to, incoming neuron
        self.weights = [random.gauss(0, 1) for _ in self.previous_layer]    # One neuron has one weight from each neuron coming into it from the previous layer
        # TODO Later we'll need a delta value

    def __repr__(self):
        return str([f'{self.previous_layer[i]} -> {self.weights[i]}' for i in range(len(self.previous_layer))])

    def update_activation(self):
        # Multiply each weight by the activation of each neuron in the previous layer, then apply logistic(sigma) function
        s = sum(self.weights[i] * self.previous_layer[i].activation for i in range(len(self.previous_layer)))
        self.activation = logistic(s)

        # Predict the output(activation) for the given list of inputs
    def predict(self, inputs):
        inputs = [1] + inputs
        for i in range(1, len(inputs)):
            self.previous_layer[i].activation = inputs[i]
        self.update_activation()
        return self.activation

        # Given inputs, this should be the correct target
    def train(self, inputs, target):
        a = self.predict(inputs)
        t = target
        delta = -a * (1 - a) * (t - a)
        for j in range(len(self.previous_layer)):
            self.weights[j] += -LEARNING_RATE * self.previous_layer[j].activation * delta


class Network:

    def __init__(self, sizes):
        """
        :param sizes: A list of the number of neurons in each layer, e.g., [2, 2, 1] for a network that can learn XOR.
        """
        self.layers = [None] * len(sizes)
        self.layers[0] = [InputNeuron() for _ in range(sizes[0])]
        for i in range(1, len(sizes)):
            self.layers[i] = [Neuron(self.layers[i-1]) for _ in range(sizes[i])]


def logistic(x):
    return 1 / (1 + math.exp(-x))


net = Network([2, 2, 1])

# n = Neuron([InputNeuron(0), InputNeuron(0)])
# n.weights = [-3, 2, 2]
#
# print(n.predict([0, 0]))
# print(n.predict([0, 1]))
# print(n.predict([1, 0]))
# print(n.predict([1, 1]))
#
# for _ in range(1000):
#     n.train([0, 0], 0)
#     n.train([0, 1], 0)
#     n.train([1, 0], 0)
#     n.train([1, 1], 1)
#
# print()
#
# print(n.predict([0, 0]))
# print(n.predict([0, 1]))
# print(n.predict([1, 0]))
# print(n.predict([1, 1]))
