import json
import numpy as np
import sa
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

def results_to_json(objetives_list, best_objetives_list, probabilities_list, temperature_list, best_objetive, best_solution, elapsed_time):
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

def run_tests_sa(name_test, iterations):
    tests = load_json(name_test)
    count_test = 1
    for test in tests:
        for i in range(1,iterations+1):
            print('   running test ' + test['NAMETEST'] + ' ' + str(i) + '/'+ str(iterations)+ ' ...')
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
            results_json = results_to_json(objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, best_solution, elapsed_time)
            save_results(results_json,'result/' + test['NAMETEST']+ '_SA_' + str(i) + '.json')
        print('Test: '+ test['NAMETEST'] + ' finalizado. ' + str(count_test) + '/7')

def run_tests_ga(name_test,iterations):
    tests = load_json(name_test)
    count_test = 1
    return True