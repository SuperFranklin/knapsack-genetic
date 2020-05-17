import random
from item import Item
import time
import knapsackClassic

# if more than 30, optimal recursive algorithm begins to get in trouble
NUMBER_OF_ITEMS = 22
MAX_ITEM_VALUE = 30
MAX_ITEM_WEIGHT = 30

ITEMS = [Item(random.randint(0, MAX_ITEM_VALUE), random.randint(0, MAX_ITEM_WEIGHT)) for x in range (0,NUMBER_OF_ITEMS)]

CAPACITY = 10*NUMBER_OF_ITEMS

POPULATION_SIZE = 2*NUMBER_OF_ITEMS

NUMBER_OF_GENERATIONS = NUMBER_OF_ITEMS * 200


def calculateKnapsackValue(target):
    total_value = 0
    total_weight = 0
    index = 0
    for i in target:
        if index >= len(ITEMS):
            break
        if i == 1:
            total_value += ITEMS[index].value
            total_weight += ITEMS[index].weight
        index += 1

    if total_weight > CAPACITY:
        return 0
    else:
        return total_value


def drawStartingPopulation(amount):
    return [drawGenotype() for _ in range(0, amount)]


def drawGenotype():
    return [random.randint(0, 1) for _ in range(0, len(ITEMS))]


def mutate(target):
    r = random.randint(0, len(target) - 1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1


def drawParent(parents, exclude):
    index = random.randint(0, len(parents) - 1)
    if index == exclude:
        return drawParent(parents, exclude)
    else:
        return parents[index]


def evolve_population(population):
    parent_eligibility = 0.2
    mutation_likelihood = 0.08
    parent_lottery = 0.05

    parent_length = int(parent_eligibility * len(population))
    parents = population[:parent_length]
    rest = population[parent_length:]

    for combination in rest:
        if parent_lottery > random.random():
            parents.append(combination)

    for p in parents:
        if mutation_likelihood > random.random():
            mutate(p)

    children = []
    desired_length = len(population) - len(parents)
    while len(children) < desired_length:
        male = drawParent(parents, -1)
        female = drawParent(parents, male)
        half = int(len(male) / 2)
        child = male[:half] + female[half:]
        if mutation_likelihood > random.random():
            mutate(child)
        children.append(child)

    parents.extend(children)
    return parents


def genetic():
    generation = 1
    population = drawStartingPopulation(POPULATION_SIZE)
    for g in range(0, NUMBER_OF_GENERATIONS):
        population = sorted(population, key=lambda x: calculateKnapsackValue(x), reverse=True)
        population = evolve_population(population)
        generation += 1
        if g == NUMBER_OF_GENERATIONS - 1:
            print("genetic solution: ", population[0])
            print("genetic value: ", calculateKnapsackValue(population[0]))

start_time = time.time()
genetic()
print("Genetic execution time: ", (time.time() - start_time), " seconds")
start_time = time.time()
print("optimal solution: ", knapsackClassic.run(ITEMS, CAPACITY))
print("Recursion execution time: ", (time.time() - start_time), " seconds")
