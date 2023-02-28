# travelling salesman problem

import random
import math
import copy
import matplotlib.pyplot as plt

# define a city class


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = math.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

# define a route class


class Route:
    def __init__(self, route, distance=0.0):
        self.route = route
        self.distance = distance
        self.fitness = 0.0

    def __len__(self):
        return len(self.route)

    def __getitem__(self, index):
        return self.route[index]

    def __setitem__(self, key, value):
        self.route[key] = value

    def __repr__(self):
        geneString = ""
        for i in range(0, len(self.route)):
            geneString += str(self.route[i]) + "-"
        return geneString

    def getDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                destinationCity = None
                if i + 1 < len(self.route):
                    destinationCity = self.route[i + 1]
                else:
                    destinationCity = self.route[0]
                pathDistance += fromCity.distance(destinationCity)
            self.distance = pathDistance
        return self.distance

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.getDistance())
        return self.fitness

# create a route


def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

# create a population


def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(Route(createRoute(cityList)))
    return population

# rank routes by fitness


def rankRoutes(population):
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = population[i].getFitness()
    return sorted(fitnessResults.items(), key=lambda x: x[1], reverse=True)

# select routes for mating pool


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

# mating pool


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

# breed routes


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

# breed routes


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(Route(child))
    return children

# mutate routes


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if (random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

# mutate population


def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(Route(mutatedInd))
    return mutatedPop

# next generation


def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

# genetic algorithm


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    progress = []
    progress.append(1 / rankRoutes(pop)[0][1])

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute, progress


# main
cityList = []

for i in range(0, 25):
    cityList.append(City(x=int(random.random() * 200),
                    y=int(random.random() * 200)))

bestRoute, progress = geneticAlgorithm(
    population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)

plt.plot(progress)
plt.ylabel('Distance')
plt.xlabel('Generation')
plt.show()
