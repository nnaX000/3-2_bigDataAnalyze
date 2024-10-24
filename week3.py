import numpy as np
list1 = [[0, 2, 5, 7],[np.nan,2,3,4]]
arr1 = np.array(list1)
print(type(list1))
print(type(arr1))
print(arr1.dtype)
print(arr1.shape)
print(arr1.ndim)
arr1 = arr1.T
print(arr1.shape)

arr1_1 = 2*np.ones((4,1), dtype=int)
print(arr1_1.dtype)


arr1_2 = 2*np.eye(4)
print(arr1_2)

arr2 = np.linspace(2,5,4, endpoint=False)
print(arr2)
arr2 = np.arange(1,21,1)
print(arr2)
arr2 = arr2.reshape(10,-1)
print(arr2)
arr2 = arr2.reshape(-1)
print(arr2)

arr = np.arange(24).reshape(2,3,4)
print(arr)


arr = np.array([[[0,  1,  2,  3],
                         [4,  5,  6,  7],
                         [8,  9, 10, 11]],
                        [[12, 13, 14, 15],
                         [16, 17, 18, 19],
                         [20, 21, 22, 23]]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.strides)


n_1_d = np.dtype([('hello', 'f8'), ('world', 'S10')])

arr3 = np.zeros(3,dtype=n_1_d)
print(arr3)
print(arr3.dtype)
arr3['hello'] = 1000
print(arr3)

a = np.float32(5.0)
print(a.dtype)
b = np.int_([1, 2, 3])
print(b.dtype)
c = np.arange(5, dtype=np.uint16)
print(c.dtype)
arr = np.array([('jin', 25, 67), ('suho', 18, 77)],
               dtype=[('name', 'U10'), ('', 'i4'), ('weight', 'f4')])
print(arr)
arr[0] = ("joon", "18", "72")
print(arr)
arr[1] = ("soohee", "21", "45")
print(arr.dtype)
arr["f1"] = [100,23]
print(arr)

arr_d = arr.dtype
print(arr_d.names)
print(arr_d.fields)


def print_offsets(d):
    print('offsets:', [d.fields[name][1] for name in d.names])
    print('itemsize:', d.itemsize)

print_offsets(np.dtype('u1,u1,i4,u1,i8,u2'))
d = np.dtype('u1,u1,i4,u1,i8,u2')
print(d)
print(d.itemsize)
print(d.fields)
print(d.names)
print(d.fields['f0'])
print(d.fields['f0'][1])
print_offsets(np.dtype('u1,u1,i4,u1,i8,u2', align=True))


a = np.array([(1, 2, 3), (4, 5, 6)], dtype='i8, f4, f8')
a[1] = (7, 8, 9)
print(a)


a = np.zeros(2, dtype='i8, f4, ?, S1')
print(a)
a[:] = 7
print(a)
a[:] = np.arange(2)
print(a)

a = np.zeros(3, dtype=[('a', 'i8'), ('b', 'f4'), ('c', 'S3')])
b = np.ones(3, dtype=[('x', 'f4'), ('y', 'S3'), ('z', 'O')])
print(a)
print(b)

b[:] = a
print(a)
print(b)


arr1 = np.arange(10)
arr2 = np.arange(9).reshape(3,3)
arr3 = np.reshape(np.arange(24), (2,3,4))


print("----------------")
print(arr1[1])
print(arr1[:6])
print(arr1[0:5])
print(arr1[::2])
print(arr1[1::2])
print(arr1[1:7:2])

print(arr1[-3:9])
print(arr1[:-3])
print(arr1[-3:2:-1])
print(arr1[5:2])

print(arr1[5:])
print(arr2[1:])

print(arr2)
print(arr2[:2, :2])
print(arr2[:, ::-1])

print(arr2[:, :])
print(arr2[1, :])
print(arr2[1, 2])

print(arr3[:2, 1:, :2])

arr1= np.array([1, 2, 3, 4, 5])
arr2 = np.array([11, 12, 13])
#print(arr1 + arr2)
arr1_nx = arr1[:, np.newaxis]
arr2_nx = arr2[:, np.newaxis]
print(arr1_nx)
print(arr2_nx)
print(arr1_nx + arr2)
print(arr2_nx + arr1)
