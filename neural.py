# Emily Tanabe, Kendal Jones, Natalie Zoz

import math
import random


LEARNING_RATE = 1


class InputNeuron:

    def __init__(self, activation=1):
        self.activation = activation
        self.delta = 0


class OutputNeuron:

    def __init__(self, previous_layer):
        self.activation = None
        self.delta = None
        self.previous_layer = [InputNeuron()] + previous_layer  # Add bias node
        self.weights = [random.gauss(0, 1) for _ in self.previous_layer]

    def update_activation(self):
        """
        Update the activation of this neuron, based on its previous layer and weights.
        """
        s = sum(self.weights[i] * self.previous_layer[i].activation for i in range(len(self.previous_layer)))
        self.activation = logistic(s)

    def update_delta(self, target):
        """
        Update the delta value for this neuron. Also, backpropagate delta values to neurons in
        the previous layer.
        :param target: The desired output of this neuron.
        """
        a = self.activation
        t = target
        self.delta = -a * (1 - a) * (t - a)
        for unit, weight in zip(self.previous_layer[1:], self.weights[1:]):
            unit.delta += weight * self.delta

    def update_weights(self):
        """
        Update the weights of this neuron.
        """
        for j in range(len(self.previous_layer)):
            self.weights[j] += -LEARNING_RATE * self.previous_layer[j].activation * self.delta


class HiddenNeuron(OutputNeuron):

    def update_delta(self):
        """
        Update the delta value for this neuron. Also, backpropagate delta values to neurons in
        the previous layer.
        :param target: The desired output of this neuron.
        """
        a = self.activation
        self.delta = a * (1 - a) * self.delta
        for unit, weight in zip(self.previous_layer[1:], self.weights[1:]):
            unit.delta += weight * self.delta


class Network:

    def __init__(self, sizes):
        """
        :param sizes: A list of the number of neurons in each layer, e.g., [2, 2, 1] for a network that can learn XOR.
        """
        self.layers = [None] * len(sizes)
        self.layers[0] = [InputNeuron() for _ in range(sizes[0])]
        for i in range(1, len(sizes) - 1):
            self.layers[i] = [HiddenNeuron(self.layers[i-1]) for _ in range(sizes[i])]
        self.layers[-1] = [OutputNeuron(self.layers[-2]) for _ in range(sizes[-1])]

    def predict(self, inputs):
        """
        :param inputs: Values to use as activations of the input layer.
        :return: The predictions of the neurons in the output layer.
        """
        outputs = []

        for i in range(len(self.layers[0])):
            self.layers[0][i].activation = inputs[i]
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.update_activation()
        for neuron in self.layers[-1]:
            outputs.append(neuron.activation)

        return outputs

    def reset_deltas(self):
        """
        Set the deltas for all units to 0.
        """
        for layer in self.layers:
            for neuron in layer:
                neuron.delta = 0

    def update_deltas(self, targets):
        """
        Update the deltas of all neurons, using backpropagation. Assumes predict has already
        been called, so all neurons have had their activations updated.
        :param targets: The desired activations of the output neurons.
        """
        for i in range(len(targets)):
            self.layers[-1][i].update_delta(targets[i])
        for i in range(len(self.layers) - 2, 0, -1):
            for n in self.layers[i]:
                n.update_delta()

    def update_weights(self):
        """
        Update the weights of all neurons.
        """
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.update_weights()

    def train(self, inputs, targets):
        """
        Feed inputs through this network, then adjust the weights so that the activations of
        the output neurons will be slightly closer to targets.
        :param inputs: A list activation values for the input units.
        :param targets: A list desired activation values for the output units.
        """
        self.predict(inputs)
        self.reset_deltas()  # Set all deltas to 0
        self.update_deltas(targets)
        self.update_weights()


def logistic(x):
    """
    Logistic sigmoid squashing function.
    """
    return 1 / (1 + math.exp(-x))


def main():
    net = Network([2, 2, 1])
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    targets = [[0], [1], [1], [0]]

    for _ in range(1000):
        for i, t in zip(inputs, targets):
            net.train(i, t)
        for i, t in zip(inputs, targets):
            print(f"{inputs}: {net.predict(i)[0]}")


if __name__ == '__main__':
    main()
