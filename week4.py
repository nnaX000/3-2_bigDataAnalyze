import numpy as np

arr = np.array(([1, 2, 3], [4, 5, 6]))
arr
np.add.reduce(arr)
np.add.reduce(arr, axis=1)


np.add.accumulate([1, 2, 3, 4, 5])
np.multiply.accumulate([1, 2, 3, 4, 5])

arr = np.arange(12).reshape((3, 4))
np.add.accumulate(arr)
np.add.accumulate(arr, axis=1)

