import numpy as np
from simulated_annealing import SimulatedAnnealing
import tsp_genetic
import animated_visualizer
from random import sample
import pandas as pd
import make_town
import matplotlib.pyplot as plt
import time

def run_sa(x):
    ##set the simulated annealing algorithm params
    temp = 1000
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 10000
   
    ##run simulated annealing algorithm with 2-opt 
    sa = SimulatedAnnealing(x, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()
    
    #animate
    animated_visualizer.animateTSP(sa.solution_history, sa.coords)
    final_solution = sa.solution_history[-1]
    print(final_solution)
    print("End Annealing")
    
    return 
def run_ga(towns, num_towns):
    total_number_towns =num_towns
    total_GA_population_size = 1000
    
    pop= tsp_genetic.createPopulation(numberOfTowns=total_number_towns, popSize=total_GA_population_size)

    elitism_rate = 0.1
    mutation_rate = 0.01
    maximum_number_generations = 1000
    stagnation_criteria = 500 

    [finalPop, finalFitnesses, bestIdvs, bestFits] = tsp_genetic.runGA(
                                population=pop[:], towns=towns, 
                                eliteRate=elitism_rate, 
                                mutationRate=mutation_rate, 
                                iterationMax=maximum_number_generations, 
                                convergenceCriteria=stagnation_criteria)

    print('\n- Total number of generations = %s' %len(bestIdvs))
    print('- Best fitness found during algorithm = %s' %np.min(bestFits))

    array = np.array(towns)
    sorted_pop = [x for _, x in sorted(zip(finalFitnesses, finalPop), reverse=True)]
    
    animated_visualizer.animateTSP(sorted_pop, array)
    final_solution = sorted_pop[-1]
    print(final_solution)
    print("End")
   
    return 

if __name__ == "__main__":
    

    num_towns =10
    town_location_limit_lowerX = 0
    town_location_limit_upperX = 200
    town_location_limit_lowerY = 0
    town_location_limit_upperY = 200
   
    sa_times_array = []
    ga_times_array = []
    array=[]

while num_towns <= 16:
    print("\n")
    print(f"Running for {num_towns} towns:")
  
    x, towns=make_town.makeTowns(nTowns=num_towns, xMin=town_location_limit_lowerX, xMax=town_location_limit_upperX, yMin=town_location_limit_lowerY, yMax=town_location_limit_upperY, RNG=False)
    
    start = time.time()
    sa_time_out= run_sa(x)
    end = time.time()
    sa_times_array.append(end- start)
    
    
    print("Starting Genetic...")
    start = time.time() 
    ga_time_out= run_ga(towns, num_towns)
    print("End Genetic...")
    end = time.time()
    ga_times_array.append(end- start)
    array.append(num_towns)
    num_towns += 2

fig, ax = plt.subplots()
ax.plot(array, sa_times_array, label='Simulated Annealing')
ax.plot(array, ga_times_array, label='Genetic Algorithm')
ax.set_xlabel("Number of Towns")
ax.set_ylabel("Runtime (s)") 

y_max = max(sa_times_array + ga_times_array)  # Find maximum runtime
y_buffer = 5  # Add a buffer for readability
ax.set_ylim(0, y_max + y_buffer)

 
ax.legend()
plt.title("Runtime vs Number of Towns")  
plt.show()