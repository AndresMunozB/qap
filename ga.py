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
    tournament_times: mu Cuantas veces se realiza el torneo, que indica 
    """
    new_population = []
    while(tournament_times>=0):
        
        # Seleccionados del torneo
        selected_individuals = []
        while(tournament_size>=0):
            random_index = randint(0, len(population) - 1)
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

def mutation(solution, probability):
    chance = random(0, 1)
    if chance <= probability:
        i = randint(0, len(solution))
        j = randint(0, len(solution))
        x = solution[i]
        y = solution[j]
        solution[i] = y
        solution[j] = x
    return solution
