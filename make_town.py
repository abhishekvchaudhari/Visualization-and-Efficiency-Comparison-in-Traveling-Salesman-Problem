import random
import numpy as np

def makeTowns(nTowns, xMin, xMax, yMin, yMax, RNG):
    towns = []
    if RNG == False:
        random.seed(a=1)
    for i in range(nTowns):
        towns.append([random.uniform(xMin, xMax), random.uniform(yMin, yMax)])
    random.seed()
    array = np.array(towns)
    return array, towns 
