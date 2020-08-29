import qap
from random import shuffle, randint, random

def generate_population(size_population, size_solution):
    population = []
    while size_population >= 0:
        solution = qap.random_solution(size_solution)
        population.append(solution)
        size_population-=1
    return population

def tournament_selection(tournament_size, tournament_times, population, d, f):
    """ 
    tournament_size: k Individuos seleccionados por torneo
    tournament_times: mu Cuantas veces se realiza el torneo, que indica los individuos de la nueva población
    """
    new_population = []
    for _ in range(tournament_times):
        # Seleccionados del torneo
        selected_individuals = []
        for j in range(tournament_size):
            random_index = randint(0, len(population) - 1)
            selected_individuals.append(population[random_index])
        # Obtener al mejor candidato
        best_individual = selected_individuals[0]
        best_fit = qap.objective_function(best_individual, d, f)
        best_index = 0
        for j in range(1, tournament_size):
            fitness = qap.objective_function(selected_individuals[j], d, f)
            if fitness <= best_fit:
                best_index = j
                best_fit = fitness
        new_population.append(selected_individuals[best_index])
    return new_population

def mutation(solution, probability):
    chance = random()
    result = solution.copy()
    if chance <= probability: 
        i = randint(0, len(result)-1) 
        j = randint(0, len(result)-1) 
        x = result[i] 
        y = result[j]
        result[i] = y
        result[j] = x
    return result

def order_one_crossover(parent_1, parent_2):
    i = randint(0, len(parent_1)-1)
    j = randint(0, len(parent_1)-1)
    if i > j:
        i, j = j, i

    print(i)
    print(j)
    offspring_1 = [-1]*len(parent_1)
    offspring_2 = [-1]*len(parent_1)
    selected_1 = parent_1[i:j+1]
    selected_2 = parent_2[i:j+1]
    offspring_1[i: j+1] = selected_1
    offspring_2[i:j+1] = selected_2
    
    not_selected_1 = list(set(parent_2)- set(selected_1))
    print(not_selected_1)
    not_selected_2 = list(set(parent_1)- set(selected_2))
    print(not_selected_2)

    index = 0
    for k in range(i):
        offspring_1[k] = not_selected_1[index]
        offspring_2[k] = not_selected_2[index]
        index+=1
    for k in range(j+1, len(parent_1)):
        offspring_1[k] = not_selected_1[index]
        offspring_2[k] = not_selected_2[index]
        index+=1  
    return offspring_1, offspring_2


