import random
import statistics
import math

target = ''

for i in range(200):
    target += str(random.randint(0, 1))

# print(target)


def individual():
    result = ''
    for _ in range(200):
        result += str(random.randint(0, 1))
    return result


def population():
    return [individual() for _ in range(1000)]


def fitness(ind):
    return math.exp(sum([a == b for a, b in zip(ind, target)]))


def min_fitness(pop):
    return min(fitness(ind) for ind in pop)


def max_fitness(pop):
    return max(fitness(ind) for ind in pop)


def avg_fitness(pop):
    return statistics.mean(fitness(ind) for ind in pop)


def select(pop, fitnesses):
    spin = random.random() * sum(fitnesses)
    for i in range(len(pop)):
        if spin < fitnesses[i]:
            return p[i]
        else:
            spin -= fitnesses[i]


def flip(bit):
    if bit == '0':
        return '1'
    else:
        return '0'


def mutate(ind):
    return ''.join([flip(b) if random.random() < 1/len(ind) else b for b in ind])


def cross(a, b):
    i = random.randint(0, len(a))
    return a[:i] + b[i:]


def evolve(p):
    fitnesses = [fitness(i) for i in p]
    return [mutate(cross(select(p, fitnesses), select(p, fitnesses))) for _ in range(len(p))]

p = population()
for i in range(100):
    p = evolve(p)
    print(math.log(avg_fitness(p)))
    print(math.log(max_fitness(p)))
    print()


p = population()
print(min_fitness(p))
print(max_fitness(p))
print(avg_fitness(p))
