import json
import numpy as np
import sa
import ga
def load_json(name_json):
    """ Load configuration from json file """
    data = {}
    with open(name_json + ".json", 'r') as file:
        data = json.load(file)
    return data

def save_results(data,name_file):
    """ Save a object as json"""
    with open(name_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return True

def results_sa_to_json(objetives_list, best_objetives_list, probabilities_list, temperature_list, best_objetive, best_solution, elapsed_time):
    data = {
        'elapsed_time': elapsed_time,
        'best_objetive': best_objetive,
        'best_solution': best_solution,
        'objetives_list': objetives_list,
        'best_objetives_list': best_objetives_list,
        'temperature_list': temperature_list,
        'probabilities_list': probabilities_list
    }
    return data
def results_ga_to_json(best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time):
    data = {
        'elapsed_time': elapsed_time,
        'best_objective': best_objective,
        'best_solution': best_solution,
        'average_objectives_list': average_objectives_list,
        'best_objective_list': best_objective_list,
    }
    return data

def run_tests_sa(name_test, iterations):
    tests = load_json(name_test)
    count_test = 1
    
    for test in tests:
        print('   test (' + str(count_test) + '/7) '+ test['NAMETEST'] + ' iniciado. ' )
        for i in range(1,iterations+1):
            print('      (' + str(i) + '/'+ str(iterations)+ ') running test ' + test['NAMETEST'] + ' ' + ' ...')
            d = np.loadtxt(test['DMATRIX'])
            f = np.loadtxt(test['FMATRIX'])
            objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time = sa.simulated_annealing(test['INITIAL_TEMPERATURE'], 
                                                                                                        test['FINAL_TEMPERATURE'], 
                                                                                                        test['MAX_ITERATIONS'], 
                                                                                                        test['COOLING_MODE'], 
                                                                                                        test['ALPHA'], 
                                                                                                        test['BETA'],
                                                                                                        test['DEBUG'], 
                                                                                                        d,
                                                                                                        f)
            results_json = results_sa_to_json(objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time)
            save_results(results_json,'result/' + test['NAMETEST']+ '_SA_' + str(i) + '.json')
        print('   test (' + str(count_test) + '/7) '+ test['NAMETEST'] + ' finalizado. ' )
        count_test += 1

def run_tests_ga(name_test,iterations):
    tests = load_json(name_test)
    count_test = 1
    for test in tests:
        print('   test (' + str(count_test) + '/7) '+ test['NAMETEST'] + ' iniciado. ' )
        for i in range(1,iterations+1):
            print('      (' + str(i) + '/'+ str(iterations)+ ') running test ' + test['NAMETEST'] + ' ' + ' ...')
            d = np.loadtxt(test['DMATRIX'])
            f = np.loadtxt(test['FMATRIX'])
            best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time = ga.evolutive_algorithm(test['POPULATION_SIZE'], 
                                                                                                    test['GENERATIONS'], 
                                                                                                    test['TOURNAMENT_SIZE'], 
                                                                                                    test['TOURNAMENT_TIMES'],
                                                                                                    test['REPRODUCTION_TIMES'], 
                                                                                                    test['MUTATION_PROBABILITY'], 
                                                                                                    test['DEBUG'],
                                                                                                    d, f)
            results_json = results_ga_to_json(best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time)
            save_results(results_json,'result/' + test['NAMETEST']+ '_ga_' + str(i) + '.json')
        print('   test (' + str(count_test) + '/7) '+ test['NAMETEST'] + ' finalizado. ' )
        count_test += 1