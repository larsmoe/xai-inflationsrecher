import matplotlib.pyplot as plt
import numpy as np

from feature_importance import feature_importance, feat_importance_as_derivate
from calculate_inflation import calc_inflation

off_weights = np.load('official_weights.npy')
official_vpi_june20 = np.load('official_vpi_june20.npy')
official_vpi_june21 = np.load('official_vpi_june21.npy')
test_weights = np.array([150, 200, 35, 300, 50, 20, 90, 5, 5, 20, 100, 100, 23, 20, 50, 50, 20, 0, 220])
print(off_weights)
print(calc_inflation(off_weights, official_vpi_june21, official_vpi_june20))
print(test_weights)
print(calc_inflation(test_weights, official_vpi_june21, official_vpi_june20))
#feat_imp = feature_importance(test_weights, off_weights, official_vpi_june21, official_vpi_june20)
#feat_imp_der = feat_importance_as_derivate(test_weights, off_weights, official_vpi_june21, official_vpi_june20)
#np.save('feat_imp_der.npy', feat_imp_der)
#for orig, weight, imp, imp_der in zip(official_vpi_june21/np.sum(official_vpi_june21), test_weights/np.sum(test_weights), feat_imp, feat_imp_der):
#    print(orig, weight, imp, imp_der)

