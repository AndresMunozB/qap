import numpy as np
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
sa.plt.show()