import numpy as np
from simulated_annealing import SimulatedAnnealing
import tsp_genetic
import animated_visualizer
import make_town

def run_sa(x):
    #set the simulated annealing algorithm params'''
    temp = 1000
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 100000
   
     ##run simulated annealing algorithm with 2-opt
    sa = SimulatedAnnealing(x, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()
    #animate 
    animated_visualizer.animateTSP(sa.solution_history, sa.coords)
    final_solution = sa.solution_history[-1]
    print(final_solution)
    print("End Annealing")
     
def run_ga(towns):
    total_number_towns =10
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
    print("End gentic")

if __name__ == "__main__":
    
    total_number_towns =10
    town_location_limit_lowerX = 0
    town_location_limit_upperX = 200
    town_location_limit_lowerY = 0
    town_location_limit_upperY = 200
    x, towns=make_town.makeTowns(nTowns=total_number_towns, xMin=town_location_limit_lowerX, xMax=town_location_limit_upperX, yMin=town_location_limit_lowerY, yMax=town_location_limit_upperY, RNG=False)
    
    print("Simulated Annealing Algorithm started ...")
    run_sa(x)
    
    print("Genetic Algorithm Started...")
    run_ga(towns)

    
   