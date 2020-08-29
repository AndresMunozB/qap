import numpy as np
import test
import ga 
"""
import sa
initial_temperature = 2000
final_temperature = 0.01
max_iterations = 1000
cooling_mode = 'LIN'
alpha = 0.85
beta = 1
debug = True

d = np.loadtxt('data/DChr12a.txt')
f = np.loadtxt('data/FChr12a.txt')
objetives_list, best_objetives_list, probabilities_list, best_objetive = sa.simulated_annealing(initial_temperature,
                        final_temperature, 
                        max_iterations, 
                        cooling_mode, 
                        alpha,
                        beta, 
                        debug, 
                        d, 
                        f)


sa.graph(objetives_list, best_objetives_list, probabilities_list, best_objetive)
sa.plt.show()"""




population_size =  50
generations =  20
tournament_size = 30
tournament_times = 50
reproduction_times = 50 
mutation_probability = 0.2

config = test.load_json('config/chr12a_ga')
d = np.loadtxt(config['DMATRIX'])
f = np.loadtxt(config['FMATRIX'])
best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time = ga.evolutive_algorithm(population_size, 
                                            config['GENERATIONS'], 
                                            config['TOURNAMENT_SIZE'], 
                                            config['TOURNAMENT_TIMES'],
                                            config['REPRODUCTION_TIMES'], 
                                            config['MUTATION_PROBABILITY'], 
                                            config['DEBUG'],
                                            d, f)

#iterations = 30
#test.run_tests_sa("test/test_chr12a",iterations)
#test.run_tests_sa("test/test_kra32",iterations)
#test.run_tests_sa("test/test_esc64a",iterations)

