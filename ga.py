import qap
from random import shuffle, randint

def generate_population(size, n):
    population = []
    while size >= 0:
        solution = qap.random_solution(n)
        population.append(solution)
        size-=1
    return population

def roulette_selection(population, d, f):
    n = len(population)
    total_fitness = 0
    probabilities = []
    for i in range(n):
        total_fitness += qap.objective_function(population[i], d, f)
    
    for i in range(n):
        probability = qap.objective_function(population[i], d, f)/total_fitness
        probabilities.append(probability)
    return probabilities

def tournament_selection(tournament_size, tournament_times, population_size, population, d, f):
    """ 
    tournament_size: k Individuos seleccionados por torneo
    tournament_times: mu Cuantas veces se realiza el torneo, que indica 
    """
    new_population = []
    while(tournament_times>=0):
        
        # Seleccionados del torneo
        selected_individuals = []
        while(tournament_size>=0):
            random_index = randint(0, population_size - 1)
            selected_individuals.append(population[random_index])
            tournament_size-=1
        
        # Obtener al mejor candidato
        best_individual = selected_individuals[0]
        best_fit = qap.objective_function(best_individual, d, f)
        for i in range(1, tournament_size):
            fitness = qap.objective_function(selected_individuals[i], d, f)
            if fitness <= best_fit:
                best_index = i
                best_fit = fitness
        new_population.append(selected_individuals[best_index])
        tournament_times-=1
    return new_population