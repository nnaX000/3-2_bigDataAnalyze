import numpy as np

a = np.zeros(3, dtype=[('a', 'f4'), ('b', 'i4'), ('c', 'S5')])
b = np.zeros(3, dtype=[('a', 'f2'), ('b', 'i2'), ('c', 'S2')])

# a 배열 생성 - c 필드를 S7으로 수정
a = np.zeros(13, dtype=[('a', 'f4'), ('b', 'i4'), ('c', 'S7')])
# b 배열 생성
b = np.zeros(10, dtype=[('a', 'f2'), ('b', 'i2'), ('c', 'S2')])

# a 배열 값 채우기
a['a'], a['b'], a['c'] = np.arange(0.5, 7, 0.5), np.arange(2, 28, 2), [b'a', b'aa', b'aaa', b'aaaa', b'aaaaa', b'aaaaa', b'aaaaa', b'aaaaaa', b'aaaaaaa', b'aaaaaaa', b'aaaaaaa', b'aaaaaaa', b'aaaaaaa']

# b 배열 값 채우기
b['a'], b['b'], b['c'] = np.array([1., 4., 9., 16., 25., 36., 49., 64., 81., 100.]), np.array([1, 32, 243, 1024, 3125, 7776, 16807, -32768, -6487, -31072]), [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j']


print(a)
print(b)