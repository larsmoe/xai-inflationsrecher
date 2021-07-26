import numpy as np

from feature_importance import feature_importance

off_weights = np.load('official_weights.npy')
official_vpi_june20 = np.load('official_vpi_june20.npy')
official_vpi_june21 = np.load('official_vpi_june21.npy')
test_weights = np.array([150, 200, 35, 300, 50, 20, 90, 5, 5, 20, 100, 100, 23, 20, 50, 50, 20, 0, 220])
print(len(test_weights), len(off_weights))
feat_imp = feature_importance(test_weights, off_weights, official_vpi_june21, official_vpi_june20)
print(feat_imp)
print(np.sum(feat_imp))