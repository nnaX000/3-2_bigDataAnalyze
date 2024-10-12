import numpy as np
x = np.arange(62500)
x = x.reshape(10, 10, 625)
result = np.mean(x, axis=2)
np.savetxt("test.csv", result, delimiter=",")