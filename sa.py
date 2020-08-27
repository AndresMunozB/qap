from random import random
import numpy as np
import qap

def acceptance_probability(delta, temperature):
    """ Calculate de acceptance probability"""
    return np.exp(- delta / temperature)

def cooling(current_temperature,initial_temperature, mode, iteration, coefficient ):
    """ Calculate the new temperature, based the mode """
    if mode == "LIN":
        return current_temperature - coefficient
    elif mode == "GEO":
        return current_temperature * coefficient
    elif mode == "LOG":
        return initial_temperature/ np.log(iteration)

def simulated_annealing(initial_temperature,
                        final_temperature, 
                        max_iterations, 
                        cooling_mode, 
                        coefficient, 
                        debug, 
                        d, 
                        f):
    """ Simulated annealing for traveling salesman problem (TSP)"""
    current_temperature = initial_temperature
    initial_solution = qap.random_solution(d.shape[0])
    current_solution = initial_solution.copy()
    best_solution = initial_solution.copy()
    current_objetive = qap.objective_function(best_solution, d, f)
    best_objetive = current_objetive

    # Memory to plot the results
    objetives_list = [current_objetive]
    best_objetives_list =  [current_objetive]
    probabilities_list = []

    while current_temperature > final_temperature:
        i = 0
        while i < max_iterations:
            candidate_solution = qap.neighbor(current_solution) # hay que cambiar esto utilizando la solucion actual
            candidate_objetive = qap.objective_function(candidate_solution, d, f)
            if debug:
                print("Step #{:>4}/{:>4} : T = {:10.2f}, cost = {:12.2f}, new_cost = {:12.2f} ...".format(i, max_iterations, current_temperature, current_objetive, candidate_objetive))
            

            delta = candidate_objetive - current_objetive     
            if delta < 0:
                current_solution = candidate_solution.copy()
                current_objetive = candidate_objetive
                if candidate_objetive < best_objetive:     
                    best_objetive = candidate_objetive
                    best_solution = candidate_solution.copy()
            else:
                probability = acceptance_probability(delta, current_temperature)
                probabilities_list.append(probability)
                if random() < probability:
                    current_solution = candidate_solution.copy()
                    current_objetive = candidate_objetive
            best_objetives_list.append(best_objetive)
            objetives_list.append(current_objetive) 
            i = i + 1
        current_temperature = cooling(current_temperature,initial_temperature,cooling_mode,i,coefficient)
    return objetives_list, best_objetives_list, probabilities_list, best_objetive