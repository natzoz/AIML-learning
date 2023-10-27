import random


# def find_greatest(g):
#     x = g[0]
#     for i in g:
#         if i > x:
#             x = i
#     return x
#
#
# grid = generate_grid(10)
# print(grid)
# print(find_greatest(grid))

def generate_grid(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, 100))
    return result


def generate_2d_grid(m, n):
    result = []
    for i in range(m):
        result.append(generate_grid(n))
    return result


def find_greatest_2d(g):
    greatest = g[0][0]
    for n in g:
        for i in n:
            if i > greatest:
                greatest = i
    return greatest


# grid = generate_2d_grid(2, 3)
# print(grid)
# print(find_greatest_2d(grid))

# depth-first search: start at root and search down the left-most side, then go back up to parents
# breadth-first search: start at root and search down through each pair of parents and leaves, row by row
# depth: how many lines between root and node

# tree = [2, [6, [7], [5], [1]], [3, [4]]]


def generate_tree(depth):
    result = [random.randint(1, 100)]
    if depth == 0:
        return result
    for i in range(random.randint(0, 3)):
        result.append(generate_tree(depth-1))
    return result


def print_tree(tree, indent):
    print(indent + str(tree[0]))
    for child in tree[1:]:
        print_tree(child, indent + " ")


# tree = generate_tree(3)
# print_tree(tree, " ")
# print(tree)


# Returns the largest element of tree, using depth-first search
def largest(tree):
    result = tree[0]
    for child in tree[1:]:
        result = max(result, largest(child))
    return result


# print(largest(tree))
