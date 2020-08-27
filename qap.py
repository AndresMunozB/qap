from random import shuffle, randint


def objective_function(solution, d, f):
    n = len(solution)
    total = 0
    for i in range(n):
        for j in range(n):
            total += f[solution[i]][solution[j]]*d[i][j]
    return total

def random_solution(n):
    """ Generate a random solution """
    initial_solution = list(range(n))
    shuffle(initial_solution)
    return initial_solution

def neighbor(solution):
    """ Generate a neighbor from one solution """
    i = randint(1,len(solution)-2)
    j = randint(i+1,len(solution)-1)    
    new_solution = solution[:i]
    aux = solution[i:j+1]
    aux.reverse()
    new_solution.extend(aux)
    new_solution.extend(solution[j+1:])
    return new_solution


