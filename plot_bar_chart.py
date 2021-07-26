import numpy as np
import matplotlib.pyplot as plt
feat_imp = np.load('feat_imp.npy')
categories = np.load('categories.npy')
fig, ax = plt.subplots()
plt.bar(range(len(feat_imp)), feat_imp)
ax.set_yticks([])
ax.set_ylabel('Feature Importance', size=20)
ax.tick_params(axis='x', rotation=90)
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, size=15)
#plt.xticks(range(len(categories)), categories, rotation=45)
plt.show()