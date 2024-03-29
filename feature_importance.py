import itertools
from math import factorial
import numpy as np
from calculate_inflation import calc_inflation
import time

def feature_importance(weights, off_weights, vpi_now, vpi_one_year_ago):
    '''
    :param weights: individual weights of a person in percent
    :param off_weights: official average weights from the StaBu
    :param vpi_now: Verbrauerpreisindex from the current month
    :param vpi_one_year_ago: Verbrauerpreisindex from a year ago
    :return:
    '''
    weights = weights/np.sum(weights)
    off_weights = off_weights/np.sum(weights)
    input_ = []
    permutations = []
    predictions = []
    #compute official inflation
    off_inflation = calc_inflation(off_weights, vpi_now, vpi_one_year_ago)
    print("Building permutations...")
    '''
    nested for loop to iterate over all possible permutations with all possible lenghts. For each permutation
    it is assumed that the goods in the permutation are bought with the percentage given by the individual. All the 
    remaining percentage is splitted as an average citizten would spend his money.
    FUTURE IDEA: All other goods are neglected and the inflation is calculated as the individual would only buy the 
    goods in the permutation 
    '''
    for r in range(len(weights) - 1):
        print(f'... for r={r}')
        for shared in itertools.combinations(range(len(weights)), r + 1):
            #calculate the total percentage of goods in this permutation
            #print(np.array(shared))
            tot_weight_permutation = np.sum(weights[list(shared)])
            x = [weights[i] if i in shared else (1-tot_weight_permutation)*off_weights[i] for i in range(len(weights))]
            input_.append(np.array(x))
            permutations.append(shared)
            predictions.append(calc_inflation(x, vpi_now, vpi_one_year_ago))

    marginals = [(prediction - off_inflation) for prediction in predictions]
    print(marginals[:5])

    sum_of_marginals = [0.0] * len(weights)
    for i, marginal in enumerate(marginals):
        for j in permutations[i]:
            sum_of_marginals[j] += marginal

    return [sum_ / len(weights) for sum_ in sum_of_marginals]

def feat_importance_as_derivate(weights, off_weights, vpi_now, vpi_one_year_ago):
    weights = weights / np.sum(weights)
    off_weights = off_weights / np.sum(off_weights)
    feat_imp = np.zeros(len(weights))
    for i in range(len(weights)):
        feat_imp[i] = (vpi_now[i] * np.sum(weights*vpi_one_year_ago) - vpi_one_year_ago[i] * np.sum(weights*vpi_now))/np.square(np.sum(weights*vpi_one_year_ago))
    return feat_imp

def feat_importance_as_intuitive_formula(weights, off_weights, vpi_now, vpi_one_year_ago):
    weights = weights / np.sum(weights)
    off_weights = off_weights / np.sum(off_weights)
    return (weights - off_weights) * (vpi_now/vpi_one_year_ago - calc_inflation(off_weights, vpi_now, vpi_one_year_ago) - 1)


