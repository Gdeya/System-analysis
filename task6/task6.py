import json
import numpy as np

def expert_matrix_generation(experts, index):
    ind = len(experts[index])
    exp = np.zeros((ind, ind))
    for i in range(ind):
        for j in range(ind):
            if experts[index][i] < experts[index][j]:
                exp[i][j] = 1
            elif experts[index][i] == experts[index][j]:
                exp[i][j] = 0.5
    return exp

def task(s):
    initial_matrix = json.loads(s)
    experts_matrices = []
    num_of_experts = len(initial_matrix[0])
    num_of_items = len(initial_matrix)
    for expert in range(len(initial_matrix)):
        experts_matrices.append(expert_matrix_generation(initial_matrix, expert))
    
    m = np.zeros((num_of_items,num_of_items))
    for i in range(num_of_items):
        for j in range(num_of_items):
            for k in range(num_of_experts):
                m[i][j] += 1/num_of_items * experts_matrices[k][i][j]

    k0 = [1/num_of_items for i in range(num_of_experts)]
    y = np.dot(m, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k1 = np.dot(1/l, y)

    while max(abs(k1-k0)) >= 0.001:
        k0 = k1
        y = np.dot(m, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k1 = np.dot(1/l, y)

    return k1