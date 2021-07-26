import numpy as np

weights = np.array([96.85,
16.96,
31.77,
196.32,
25.92,
24.77,
11.54,
31.56,
70.7,
23.69,
27.41,
26.62,
20.81,
45.34,
24.98,
46.13,
22.22,
22.88,
233.53
])
print(weights.shape, np.sum(weights))
np.save('official_weights.npy', weights)