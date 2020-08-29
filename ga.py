import qap
from random import shuffle, randint, random

def generate_population(population_size, size_solution):
    population = []
    while population_size >= 0:
        solution = qap.random_solution(size_solution)
        population.append(solution)
        population_size-=1
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

def swap(solution):
    result = solution.copy()
    i = randint(0, len(result)-1) 
    j = randint(0, len(result)-1) 
    x = result[i] 
    y = result[j]
    result[i] = y
    result[j] = x
    return result

def mutation(population, probability):
    new_population = population.copy()
    for i in range(len(population)):
        if random() <= probability: 
            new_population[i] = swap(new_population[i])
    return new_population
    
def order_one_crossover(parent_1, parent_2):
    i = randint(0, len(parent_1)-1)
    j = randint(0, len(parent_1)-1)
    if i > j:
        i, j = j, i
    offspring_1 = [-1]*len(parent_1)
    offspring_2 = [-1]*len(parent_1)
    selected_1 = parent_1[i:j+1]
    selected_2 = parent_2[i:j+1]
    offspring_1[i: j+1] = selected_1
    offspring_2[i:j+1] = selected_2
    
    not_selected_1 = list(set(parent_2)- set(selected_1))
    not_selected_2 = list(set(parent_1)- set(selected_2))

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

def reproduction(selected_population, reproduction_times):
    new_population = []
    for _ in range(reproduction_times):
        i = randint(0, len(selected_population)-1)
        j = randint(0, len(selected_population)-1)
        offspring_1, offspring_2 = order_one_crossover(selected_population[i], selected_population[j])
        new_population.append(offspring_1)
        new_population.append(offspring_2)
    return new_population

def k_best(population,k,d,f):
    objects = []
    for i in range(len(population)):
        objects.append({"solution": population[i], "objective_value": qap.objective_function(population[i],d,f)})
    objects.sort(key=lambda x: x['objective_value'])
    return [o['solution'] for o in objects[0:k]]

def replace(population, new_population,population_size,d,f,):
    result = []
    i = population_size * 0.3
    j = population_size * 0.7
    result.extend(k_best(population,int(i),d,f))
    result.extend(k_best(new_population,int(j),d,f))
    return result

def evolutive_algorithm(population_size, generations, tournament_size, tournament_times,reproduction_times, mutation_probability, d, f):
    population = generate_population(population_size, d.shape[0])
    best_objective_list = [] # qap.objective_function(k_best(population,1,d,f),d,f)
    for _ in range(generations):
        new_population = tournament_selection(tournament_size,tournament_times,population,d,f) #tournament_time deberia ser 50
        new_population = reproduction(new_population,reproduction_times) # si reproduction_times es 25 entonces new_population es 50
        new_population = mutation(new_population,mutation_probability) # probabilidad del 10% aprox
        population =  replace(population,new_population,population_size,d,f) # 50% mejores de generacion anterior y nueva
        best_solution = k_best(population,1,d,f)[0]
        best_objective_list.append(qap.objective_function(best_solution,d,f))
    return best_objective_list



