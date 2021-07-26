import matplotlib.pyplot as plt
import numpy as np

from feature_importance import feature_importance

off_weights = np.load('official_weights.npy')
official_vpi_june20 = np.load('official_vpi_june20.npy')
official_vpi_june21 = np.load('official_vpi_june21.npy')
test_weights = np.array([150, 200, 35, 300, 50, 20, 90, 5, 5, 20, 100, 100, 23, 20, 50, 50, 20, 0, 220])
feat_imp = feature_importance(test_weights, off_weights, official_vpi_june21, official_vpi_june20)
for orig, weight, imp in zip(official_vpi_june21/np.sum(official_vpi_june21), test_weights/np.sum(test_weights), feat_imp):
    print(orig, weight, imp)
