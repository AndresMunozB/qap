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

def results_sa_to_json(objective_list, best_objective_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time,neighbors):
    data = {
        'elapsed_time': elapsed_time,
        'best_objective': best_objective,
        'neighbors': neighbors,
        'best_solution': best_solution,
        'objective_list': objective_list,
        'best_objective_list': best_objective_list,
        'temperature_list': temperature_list,
        'probabilities_list': probabilities_list
    }
    return data
def results_ga_to_json(best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time,neighbors):
    data = {
        'elapsed_time': elapsed_time,
        'best_objective': best_objective,
        'neighbors': neighbors,
        'best_solution': best_solution,
        'average_objectives_list': average_objectives_list,
        'best_objective_list': best_objective_list
    }
    return data

def run_tests_sa(name_test, iterations):
    tests = load_json(name_test)
    count_test = 1
    
    for test in tests:
        name_test = test['NAMETEST']
        print(f'   test ({count_test}/{len(tests)}) {name_test} started. ' )
        for i in range(1,iterations+1):
            print(f'      ({i}/{iterations}) running test {name_test} ...')
            d = np.loadtxt(test['DMATRIX'])
            f = np.loadtxt(test['FMATRIX'])
            objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time, neighbors = sa.simulated_annealing(test['INITIAL_TEMPERATURE'], 
                                                                                                        test['FINAL_TEMPERATURE'], 
                                                                                                        test['MAX_ITERATIONS'], 
                                                                                                        test['COOLING_MODE'], 
                                                                                                        test['ALPHA'], 
                                                                                                        test['BETA'],
                                                                                                        test['DEBUG'], 
                                                                                                        d,
                                                                                                        f)
            results_json = results_sa_to_json(objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time, neighbors)
            iteration_str = str(i).zfill(3)
            save_results(results_json,f'result/{name_test}_sa_{iteration_str}.json')
        print(f'   test ({count_test}/{len(tests)}) {name_test} finished. ' )
        count_test += 1

def run_tests_ga(name_test,iterations):
    tests = load_json(name_test)
    count_test = 1
    for test in tests:
        name_test = test['NAMETEST']
        print(f'   test ({count_test}/{len(tests)}) {name_test} started. ' )
        for i in range(1,iterations+1):
            print(f'      ({i}/{iterations}) running test {name_test} ...')
            d = np.loadtxt(test['DMATRIX'])
            f = np.loadtxt(test['FMATRIX'])
            best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time, neighbors = ga.evolutive_algorithm(test['POPULATION_SIZE'], 
                                                                                                    test['GENERATIONS'], 
                                                                                                    test['TOURNAMENT_SIZE'], 
                                                                                                    test['TOURNAMENT_TIMES'],
                                                                                                    test['REPRODUCTION_TIMES'], 
                                                                                                    test['MUTATION_PROBABILITY'], 
                                                                                                    test['DEBUG'],
                                                                                                    test['SAME_BEST'],
                                                                                                    d, f)
            results_json = results_ga_to_json(best_objective_list, average_objectives_list, best_solution, best_objective, elapsed_time, neighbors)
            iteration_str = str(i).zfill(3)
            save_results(results_json,f'result/{name_test}_ga_{iteration_str}.json')
        print(f'   test ({count_test}/{len(tests)}) {name_test} finished. ' )
        count_test += 1


#TESTS

#iterations = 1
#EVOLUTIVE ALGORITHM
#test.run_tests_ga("test/test_ga_chr12a",iterations)
#test.run_tests_ga("test/test_ga_kra32",iterations)
#test.run_tests_ga("test/test_ga_esc64a",iterations)


#SIMULATED ANNEALING
#test.run_tests_sa("test/test_sa_chr12a",iterations)
#test.run_tests_sa("test/test_sa_kra32",iterations)
#test.run_tests_sa("test/test_sa_esc64a",iterations)

#run_tests_sa("test/test_sa",iterations)