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
iterations = 30
test.run_tests_sa("test/test_chr12a",iterations)
test.run_tests_sa("test/test_kra32",iterations)
test.run_tests_sa("test/test_esc64a",iterations)

"""d = np.loadtxt('data/DChr12a.txt')
f = np.loadtxt('data/FChr12a.txt')
size_population = 12
size_solution = 12
population = ga.generate_population(size_population,size_solution)
selected_population = ga.tournament_selection(6, 10, population, d, f)

#mutation = ga.mutation(new_population[0], 0.8)
offspring_population = ga.reproduction(selected_population,3)
#print(offspring_population)
population_size =  50
generations =  20
tournament_size = 20
tournament_times = 50
reproduction_times = 50 
mutation_probability = 0.2
best_objective_list = ga.evolutive_algorithm(population_size, 
                                            generations, 
                                            tournament_size, 
                                            tournament_times,
                                            reproduction_times, 
                                            mutation_probability, 
                                            d, f)
print(best_objective_list)

"""