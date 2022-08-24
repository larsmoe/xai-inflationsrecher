import numpy as np
import matplotlib.pyplot as plt
feat_imp = np.load('feat_imp.npy')
feat_imp_der = np.load('feat_imp_der.npy')
categories = np.load('categories.npy')
fig, ax = plt.subplots()

plt.bar(range(len(feat_imp)), feat_imp)
ax.set_yticks([])
ax.set_ylabel('Feature Importance', size=20)
ax.tick_params(axis='x', rotation=90)
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, size=15)
#plt.xticks(range(len(categories)), categories, rotation=45)
fig2, ax2 = plt.subplots()
plt.bar(range(len(feat_imp_der)), feat_imp_der)
ax2.set_yticks([])
ax2.set_ylabel('Feature Importance', size=20)
ax2.tick_params(axis='x', rotation=90)
ax2.set_xticks(range(len(categories)))
ax2.set_xticklabels(categories, size=15)
plt.show()