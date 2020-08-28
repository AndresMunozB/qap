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
iterations = 15
#test.run_tests("test/test_chr12a",iterations)
#test.run_tests("test/test_esc64a",iterations)
#test.run_tests("test/test_tai100a",iterations)

d = np.loadtxt('data/DChr12a.txt')
f = np.loadtxt('data/FChr12a.txt')
size_population = 12
size_solution = 12
population = ga.generate_population(size_population,size_solution)
new_population = ga.roulette_selection(12,population,d,f)
print(new_population)

