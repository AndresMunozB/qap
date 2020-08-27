import numpy as np
import sa

initial_temperature = 50000
final_temperature = 0.1
max_iterations = 20
cooling_mode = 'GEO'
coefficient = 0.85
debug = True

d = np.loadtxt('data/DChr12a.txt')
f = np.loadtxt('data/FChr12a.txt')
objetives_list, best_objetives_list, probabilities_list, best_objetive = sa.simulated_annealing(initial_temperature,
                        final_temperature, 
                        max_iterations, 
                        cooling_mode, 
                        coefficient, 
                        debug, 
                        d, 
                        f)

print(best_objetive)
