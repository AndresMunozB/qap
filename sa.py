from random import random
import numpy as np
import qap
import matplotlib.pyplot as plt
from time import time

def acceptance_probability(delta, temperature):
    """ Calculate de acceptance probability"""
    return np.exp(- delta / temperature)

def cooling(current_temperature,initial_temperature, mode, iteration, alpha, beta):
    """ Calculate the new temperature, based the mode """
    if mode == "LIN":
        return current_temperature - beta
    elif mode == "GEO":
        return current_temperature * alpha
    elif mode == "LOG":
        return initial_temperature/ np.log(iteration)

def simulated_annealing(initial_temperature,
                        final_temperature, 
                        max_iterations, 
                        cooling_mode, 
                        alpha,
                        beta, 
                        debug, 
                        d, 
                        f):
    """ Simulated annealing for traveling salesman problem (TSP)"""
    start_time = time()
    current_temperature = initial_temperature
    initial_solution = qap.random_solution(d.shape[0])
    current_solution = initial_solution.copy()
    best_solution = initial_solution.copy()
    current_objective = qap.objective_function(best_solution, d, f)
    best_objective = current_objective

    # Memory to plot the results
    objectives_list = [current_objective]
    best_objectives_list =  [current_objective]
    probabilities_list = []
    temperature_list = [current_temperature]

    while current_temperature > final_temperature:
        i = 0
        while i < max_iterations:
            candidate_solution = qap.neighbor(current_solution) # hay que cambiar esto utilizando la solucion actual
            candidate_objective = qap.objective_function(candidate_solution, d, f)
            if debug:
                print("Step #{:>4}/{:>4} : T = {:10.2f}, cost = {:12.2f}, new_cost = {:12.2f} ...".format(i, max_iterations, current_temperature, current_objective, candidate_objective))
            delta = candidate_objective - current_objective     
            if delta < 0:
                current_solution = candidate_solution.copy()
                current_objective = candidate_objective
                if candidate_objective < best_objective:     
                    best_objective = candidate_objective
                    best_solution = candidate_solution.copy()
            else:
                probability = acceptance_probability(delta, current_temperature)
                probabilities_list.append(probability)
                if random() < probability:
                    current_solution = candidate_solution.copy()
                    current_objective = candidate_objective
            i = i + 1
            best_objectives_list.append(best_objective)
            objectives_list.append(current_objective)
            temperature_list.append(current_temperature) 
        current_temperature = cooling(current_temperature,initial_temperature,cooling_mode,i, alpha, beta)
    elapsed_time = time() - start_time
    return objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time

def graph(objetives_list, best_objetives_list, probabilities_list, best_objetive):
    plt.figure(1)
    plt.subplot(3, 1, 1)
    graficoMejores = plt.plot(best_objetives_list)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(u"Simulated annealing TSP") 
    plt.ylabel(u"Mejor valor")
    plt.subplot(3, 1, 2)
    grafico = plt.plot(objetives_list)
    plt.setp(grafico,"linestyle","none","marker","s","color","r","markersize","1")
    plt.ylabel(u"Valor actual")
    plt.subplot(3, 1, 3)
    grafico = plt.plot(probabilities_list)
    plt.setp(grafico,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Probabilidad")
    plt.xlabel(u"Valor óptimo : " + str(best_objetive))
    return True