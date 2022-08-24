import numpy as np
from calculate_inflation import calc_inflation

test_weights = np.load('official_weights.npy')[:4]
test_vpi_aya = np.load('official_vpi_june20.npy')[:4]
test_vpi_now = np.load('official_vpi_june21.npy')[:4]
test_weights = [0, 0, 1, 0]
print(calc_inflation(test_weights, test_vpi_now, test_vpi_aya))