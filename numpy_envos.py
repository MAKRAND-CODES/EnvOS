import numpy as np
environment = np.array([
    [42,32, 4.5],
    [36,78, 8.9],
    [67,89, 9.8],
    [23,45, 7.9],
    [16,29, 9.7]
])
#print(environment[])
print(environment.shape)
print(np.mean(environment))
print(np.max(environment))
print(np.min(environment))