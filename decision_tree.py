import math

ATTRIBUTES = ('Alternative', 'Bar', 'Friday/Saturday', 'Hungry', 'Patrons', 'Price', 'Raining',
              'Reservation', 'Type', 'Wait')


class Datum:
    def __init__(self, target, *values):
        self.target = target
        self.attributes = dict(zip(ATTRIBUTES, values))


data = (Datum(True, True, False, False, True, 'Some', '$$$', False, True, 'French', '0-10'),
        Datum(False, True, False, False, True, 'Full', '$', False, False, 'Thai', '30-60'),
        Datum(True, False, True, False, False, 'Some', '$', False, False, 'Burger', '0-10'),
        Datum(True, True, False, True, True, 'Full', '$', True, False, 'Thai', '10-30'),
        Datum(False, True, False, True, False, 'Full', '$$$', False, True, 'French', '>60'),
        Datum(True, False, True, False, True, 'Some', '$$', True, True, 'Italian', '0-10'),
        Datum(False, False, True, False, False, 'None', '$', True, False, 'Burger', '0-10'),
        Datum(True, False, False, False, True, 'Some', '$$', True, True, 'Thai', '0-10'),
        Datum(False, False, True, True, False, 'Full', '$', True, False, 'Burger', '>60'),
        Datum(False, True, True, True, True, 'Full', '$$$', False, True, 'Italian', '10-30'),
        Datum(False, False, False, False, False, 'None', '$', False, False, 'Thai', '0-10'),
        Datum(True, True, True, True, True, 'Full', '$', False, False, 'Burger', '30-60'))


def impurity(data):
    '''
    :param data: A sequence of Datum objects.
    :return: The Gini impurity of the data, as per equation 6.1 on p. 197 of Géron.
    '''

    if len(data) == 0:
        return 0

    true_sum, false_sum = 0, 0
    n = len(data)
    for datum in data:
        if datum.target:
            true_sum += 1
        else:
            false_sum += 1

    gini_sum = (true_sum / n) ** 2 + (false_sum / n) ** 2
    gini = 1 - gini_sum
    return gini


def split_cost(data, attribute, value):
    '''
    :param data: A sequence of Datum objects.
    :param attribute: An attribute on which to split.
    :param value: The value to distinguish from other values at this node.
    :return: The cost of splitting in this way, as per equation 6.2 on p. 200 of Géron.
    '''
    left = []
    right = []
    n = len(data)

    for datum in data:
        if datum.attributes[attribute] == value:
            left.append(datum)
        else:
            right.append(datum)

    m_left = len(left) / n
    m_right = len(right) / n
    j = (m_left * impurity(left)) + (m_right * impurity(right))
    return j


def best_split(data):
    '''
    :param data: A sequence of Datum objects.
    :return: The best attribute and value to split on at this node.
    '''
    best_value = 1
    best_split_cost = 1
    best_attribute = ATTRIBUTES[0]

    for attribute in ATTRIBUTES:
        for value in set(d.attributes[attribute] for d in data):
            if split_cost(data, attribute, value) < best_split_cost:
                best_split_cost = split_cost(data, attribute, value)
                best_value = value
                best_attribute = attribute

    return best_attribute, best_value


class Tree:
    def __init__(self, data):
        # TODO You have to write this to build the tree from data
        # Hint: It's recursive, because you may be building subtrees

        self.data = data
        self.gini = impurity(data)
        self.split = None

        if len([datum for datum in data if datum.target]) / len(data) >= .5:
            self.cat = True
        else:
            self.cat = False

        if self.gini != 0:
            self.split = best_split(data)
            self.left_subtree = Tree([datum for datum in self.data if datum.attributes[self.split[0]] == self.split[1]])
            self.right_subtree = Tree(
                [datum for datum in self.data if datum.attributes[self.split[0]] != self.split[1]])

        # if impurity(data) == 0:
        #     self.attribute = None
        #     self.prediction = data.target[self.attribute]
        # else:
        #     split = best_split(data)
        #     self.attribute = split
        #     self.value = self.attribute
        #     for datum in data:
        #         self.left = self.__init__(datum.attributes[split])
        #         self.right = self.__init__(datum.target)

    def __repr__(self, indent=''):
        # TODO You have to write this
        # Hint: It's recursive. A recursive call might be something like:
        # self.left.__repr__(indent + '  ')
        if self.split is None:
            return str(self.cat)

        start = self.split[0] + '==' + str(self.split[1]) + '?' + '\n'
        left = indent + 'If True, ' + self.left_subtree.__repr__(indent + '  ') + '\n'
        right = indent + 'If False, ' + self.right_subtree.__repr__(indent + '  ') + '\n'
        return start + left + right

    def predict(self, datum):
        '''
        :param datum: A Datum object.
        :return: The tree's prediction for the attribute values of datum.
        '''
        # TODO You have to write this
        # Hint: You guessed it, recursive!

        if self.split is None:
            return self.cat

        if datum.attributes[self.split[0]] == self.split[1]:
            return self.left_subtree.predict(datum)
        else:
            return self.right_subtree.predict(datum)

        # best_values = []
        # best_prediction = 1
        #
        # for attribute in ATTRIBUTES:
        #     if split_cost(datum, attribute, datum.prediction) < best_prediction:
        #         best_prediction = split_cost(datum, attribute, datum.prediction)
        #         best_values.append(datum.prediction)
        #
        # return best_values


def main():
    tree = Tree(data)
    print(tree)  # This implicitly calls your __repr__ method


if __name__ == '__main__':
    main()
