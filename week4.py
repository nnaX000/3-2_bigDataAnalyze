import numpy as np

arr = np.array(([1, 2, 3], [4, 5, 6]))
print(arr.shape)
print(np.add.reduce(arr))
print(np.add.reduce(arr, axis=1))

print(np.add.accumulate(arr,axis=1))

print(np.add.accumulate([1, 2, 3, 4, 5]))
print(np.multiply.accumulate([1, 2, 3, 4, 5]))

print(np.subtract.accumulate([1,2,3,4,5]))
print(np.remainder.accumulate([1123, 18, 9, 5, 3]))


arr = np.arange(12).reshape((3, 4))
print(np.add.accumulate(arr))
print(np.add.accumulate(arr, axis=1))


print(np.subtract(1.0, 4.0))
arr1 = np.arange(9.0).reshape((3, 3))
arr2 = np.arange(3.0)
print(np.subtract(arr1, arr2))


arr1 = range(6)
print(arr1)
print(np.power(arr1, 3))
arr2 = [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
print(np.power(arr1, arr2))



import numpy as np
import matplotlib.pyplot as plt


arr = np.linspace(0, 30,   20001)
plt.plot(arr, np.sin(arr))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.grid()
plt.show()


arr = np.arange(10)
print(arr)
v1 = arr[1:2].copy()
print(v1)
arr[1] = 2
print(v1)
v2 = arr[1::3]
print(v2)
arr[7] = 10
print(v2)


arr = np.ones(4, dtype=np.uint8)
print(arr)
print(arr.view(np.uint16))
print(arr.view(np.uint32))


arr = np.ones(4, dtype=np.uint8)
print(arr.dtype)
print(arr.astype(np.uint16).dtype)
print(arr.astype(np.uint32).dtype)


arr = np.arange(4, dtype=np.uint16).reshape(2, 2)
print(arr)
print(arr.view(np.uint8))
print(arr * 100)
print((arr * 100).view(np.uint8))


arr = np.arange(10, dtype='int16')
print(arr)
v1 = arr.view('int32')
print(v1)
v1 += 1
print(v1.view('int16'))
v2 = arr.view('int8')
print(v2)



a = np.array([[1.0, 2.0, 3.0]])
b = np.array([[2.0, 2.0, 2.0]])
arr = a.T * b.T
print(arr)


a = np.array([1.0, 2.0, 3.0])
b = 2.0
print(a * b)

print("--------------------------------------")
arr1 = np.arange(4)
arr2 = arr1.reshape(4, 1)
arr3 = np.ones(5)
arr4 = np.ones((3, 4))
print(arr1.shape)
print(arr3.shape)
#arr1 + arr3
print(arr2.shape)
print((arr2 + arr3).shape)
print(arr2 + arr3)
print(arr4.shape)
print((arr1 + arr4).shape)
print(arr1 + arr4)

arr = np.array([0, 1, 2, 3])
print(arr.shape)
arr_1 = arr[np.newaxis, :]
print(arr_1)
arr_2 = arr[:, np.newaxis]
print(arr_2)

arr1 = np.array([0, 1, 2, 3])
arr2 = np.array([10, 20, 30])
arr11 = arr1[:, np.newaxis]
print(arr11 + arr2)



arr = np.arange(10)
arr_br = arr - arr[:, np.newaxis]
print(arr_br)

import numpy as np
import matplotlib.pyplot as plt


arr1 = np.arange(10)
arr2 = np.arange(7)
arr_img = np.sqrt(arr1[:, np.newaxis]**2 + arr2**2)
plt.pcolor(arr_img)
#plt.pcolor(arr_br)
plt.colorbar()
plt.axis('equal')
plt.show()

print("----------------------------------")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
print(np.concatenate((arr1, arr2), axis=0))
print(np.concatenate((arr1, arr2.T), axis=1))
print(np.concatenate((arr1, arr2), axis=None))


print(np.hstack((arr1, arr2.T)))
print(np.vstack((arr1, arr2)))



dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Jin', 175, 59), ('Suho', 185, 19),('Naeun', 162, 28)]
arr = np.array(values, dtype=dtype)
arr.sort(order=['name'])
print(arr)
print(np.sort(arr, order=['age']))

arr = np.array([15,16,16,17,19,20,22,35,43,45,55,59,60,75,88])
print(np.histogram(arr, bins=[0,20,40,60,80,100]))
a, b = np.histogram(arr, bins=[0,20,40,60,80,100])
print(a)
print(b)


import matplotlib.pyplot as plt
import numpy as np
arr = np.array([15,16,16,17,19,20,22,35,43,45,55,59,60,75,88])
plt.hist(arr, bins=[0, 20, 40, 60, 80, 100])
plt.title('numbers depending on ages')
plt.grid()
plt.show()

arr1 = arr2 = arr3 = np.arange(0.0, 5.0, 1.0)
np.savetxt('test1.csv', arr1, delimiter=',') # arr1 is array
np.savetxt('test2.csv', (arr1,arr2,arr3)) # same size of 2D array
np.savetxt('test3.csv', arr1, fmt='%1.4e') # exponential
arr4= np.loadtxt('test1.csv')
arr5= np.loadtxt('test2.csv')
arr6= np.loadtxt('test3.csv')
print(arr4)
print(arr5)
print(arr6)


import scipy.misc
import matplotlib.pyplot as plt
face = scipy.misc.face()
print(face.shape)
print(face.max(), face.min(), face.mean())
print(face.dtype)
plt.gray()
plt.imshow(face)
plt.show()


import imageio
imageio.imwrite('face.png', face)
face1 = imageio.imread('face.png')
print(type(face1))
print(face1.dtype, face1.shape)
face1.tofile('face1.raw')
arr = np.fromfile('face1.raw', dtype=np.uint8)
print(arr)
print(arr.shape)
arr.shape = (768, 1024, 3)
print(arr)
print(arr.shape)


import scipy.misc
import matplotlib.pyplot as plt
face1 = scipy.misc.face(gray=True)
plt.imshow(face1, cmap=plt.cm.gray)
plt.axis('off')
plt.show()

plt.imshow(face1, cmap=plt.cm.gray, vmin=20, vmax=100)
plt.axis('off')
plt.show()

face1 = scipy.misc.face(gray=True)
plt.imshow(face1[0:500, 400:900], cmap=plt.cm.gray, interpolation='nearest')
plt.show()

import numpy as np
import scipy.misc
import scipy.ndimage
import matplotlib.pyplot as plt


arr = scipy.misc.face(gray=True)
arr_flipud = np.flipud(arr)
arr_rotate = scipy.ndimage.rotate(arr, 45)
plt.imshow(arr_flipud, cmap=plt.cm.gray)
plt.show()
plt.imshow(arr_rotate, cmap=plt.cm.gray)
plt.show()
