import numpy as np
import test 
import ga 
import sa 


"""name_json = "config/ga_esc64a"
config = test.load_json(name_json)
d = np.loadtxt(config['DMATRIX'])
f = np.loadtxt(config['FMATRIX'])
best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time, neighbors = ga.evolutive_algorithm(config['POPULATION_SIZE'], 
                                                                                        config['GENERATIONS'], 
                                                                                        config['TOURNAMENT_SIZE'], 
                                                                                        config['TOURNAMENT_TIMES'],
                                                                                        config['REPRODUCTION_TIMES'], 
                                                                                        config['MUTATION_PROBABILITY'], 
                                                                                        config['DEBUG'],
                                                                                        config['SAME_BEST'],
                                                                                        d, f)
ga.graph(best_objective_list, average_objectives_list,best_objective, elapsed_time)
print(f"time: {elapsed_time} - neighbors: {neighbors} - best_objective: {best_objective}")"""

"""
name_json = "config/sa_chr12a"
config = test.load_json(name_json)
d = np.loadtxt(config['DMATRIX'])
f = np.loadtxt(config['FMATRIX'])
objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time, neighbors = sa.simulated_annealing(config['INITIAL_TEMPERATURE'], 
                                                                                            config['FINAL_TEMPERATURE'], 
                                                                                            config['MAX_ITERATIONS'], 
                                                                                            config['COOLING_MODE'], 
                                                                                            config['ALPHA'], 
                                                                                            config['BETA'],
                                                                                            config['DEBUG'], 
                                                                                            d,
                                                                                            f)
print(f"time: {elapsed_time} - neighbors: {neighbors} - best_objective:{best_objective}")
sa.graph(objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, elapsed_time)"""

test.run_tests_ga("test/test_ga_esc64a",30)
test.run_tests_ga("test/test_sa",30)
test.run_tests_ga("test/test_ga",30)





