import numpy as np
import pandas as pd


ser = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(ser)
print(ser.values)
print(ser.index)
print(ser.shape)

ser1 = pd.Series([2,3,4,5,6], index=['b','c','d','e','f'])
print(ser1)

df = pd.DataFrame([ser,ser, ser1, ser1], index=['a1', 'b1','c1','d1'])
print(df)

print(df.values)
print(df.index)

da = {'a' : 0., 'b' : 1., 'c' : 2.}
print(pd.Series(da))
print(pd.Series(da, index=['b', 'c', 'd', 'a']))

print(np.power(10,pd.DataFrame(np.random.randn(12).reshape(3,4))))

print(ser[0])
print(ser['a'])

print(ser[0:2])
print(ser['a':'c'])


ser2 = pd.Series(np.random.randn(5),  name='seoul')
print(ser2)
ser3 = ser.rename('busan')
print(ser3)

d = {'one': pd.Series([1., 2., 3.],
                       index=['a', 'b', 'c']),
              'two': pd.Series([1., 2., 3., 4.],
                       index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

df1 = pd.DataFrame(d, index=['a','c','d'], columns=['one','two'])
print(df1)
df2 = pd.DataFrame(d, index=['b','d','e'], columns=['three','two'])
print(df2)
df3 = df1 + df2
print(df3)


arr = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
arr[:] = [(1, 2., 'Hello'), (2, 3., 'World')]
print(arr)
print(pd.DataFrame(arr))
print(pd.DataFrame(arr, index=['first', 'second']))
print(pd.DataFrame(arr, columns=['C', 'A', 'B']))

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data))

data=pd.DataFrame({('a','b'): {('A','B'): 1, ('A','C'): 2},
                       ('a','a'): {('A','C'): 3, ('A','B'): 4},
                       ('a','c'): {('A','B'): 5, ('A','C'): 6},
                       ('b','a'): {('A','C'): 7, ('A','B'): 8},
                       ('b','b'): {('A','D'): 9, ('A','B'): 10}})

print(data)

d = {'one': pd.Series([1., 2., 3.],
                       index=['a', 'b', 'c']),
              'two': pd.Series([1., 2., 3., 4.],
                       index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

print(df['one'])
print(df['two'])
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
df['four'] = 0
df['whatever'] = 'A+'
print(df)

del df['flag']
df.pop('whatever')
print(df)
df['truncated_one'] = df['one'][:2]
print(df)
df.insert(1, 'hi', df['one'])
print(df)
df=df.drop(["d"],axis=0)
print(df)
#print(df.loc(0))
print(df.iloc(1))


df = pd.DataFrame(np.random.randn(5, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(3, 3), columns=['A', 'B', 'C'])
print(df + df2)
print(df)
print(df.T)

df = pd.DataFrame(np.arange(12).reshape(2, 6), columns=list('ABCDEF'))
print(df)
print(df.index)

ser = pd.Series(np.random.randn(1000))
print(ser.head())
print(ser.tail(3))

ind = pd.date_range('1/1/2019', periods=15)
ser = pd.Series(np.random.randn(15))
df = pd.DataFrame(np.random.randn(15, 3), index=ind, columns=['A', 'B', 'C'])
print(df)

print("----------------------------------------------------------")

df = pd.DataFrame({'one':pd.Series(np.random.randn(2),index=['a','b']),
                                                   'two':pd.Series(np.random.randn(3),index=['a','b','c']),
                                                   'three':pd.Series(np.random.randn(2),index=['b','c'])})
print(df)
print(df.iloc[1])
print(df['two'])
row = df.iloc[1]
col = df['two']
print(row, col)
print(df.loc['b'])

d = {'one': [1., 2., np.nan],
                       'two': [3., 2., 1.],
                       'three': [np.nan, 1., 1.]}
df = pd.DataFrame(d, index=list('abc'))
print(df)

d1 = {'one': pd.Series([1.,2.], index=['a','b']),
                          'two': pd.Series([1.,1.,1.], index=['a','b','c']),
                          'three': pd.Series([2.,2.,2.], index=['a','b','c'])}
df1 = pd.DataFrame(d1)
print(df1)

print(df+df1)
print(df.add(df1, fill_value=0))


df = pd.DataFrame({'angles': [0, 3, 4], 'degrees': [360, 180, 360]},
                                          index=['circle', 'triangle', 'rectangle'])

df1 = df.sub(pd.Series([1, 2, 3], index=['circle', 'triangle', 'rectangle']), axis='index')

print(df1)

print("-----------------------------------")
print(df1.mean(1))
print(df1.sum(0,skipna=True))
print(df1.std())
print(df1.to_numpy().std(0))


ser = pd.Series(np.random.randn(500))
ser[20:500] = np.nan
ser[10:20] = 5
print(ser.nunique())
print(ser.describe())

ser = pd.Series(np.random.randn(1000))
ser[::2] = np.nan
print(ser.describe(percentiles=[0.10, 0.25, .30, .65, .78]))


ser = pd.Series(['a','a','b','c','c',np.nan, 'c', 'd'])
print(ser.describe())
df = pd.DataFrame({'a': ['Yes', 'Yes', 'No', 'No'], 'b': range(4)})
print(df.describe(include='all'))



data = np.random.randint(0, 7, size=30)
ser1 = pd.Series(data)
print(ser1.value_counts())
print(pd.value_counts(data))


df1 = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'),
                       index=pd.date_range('20190701', periods=5))
print(df1)
print(df1.loc['20190702':'20190703'])


df1 = pd.DataFrame(np.random.randn(5, 4), index=list('abcde'), columns=list('ABCD'))
print(df1)
df1_row = ['a', 'b', 'd']
df1_column = ["B","C"]
df2 = df1.loc[df1_row, df1_column]
print(df2)

print("--------------------")
ser = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])
print(ser)
print(ser.loc[3:5])
print(ser.iloc[1:4])
print(ser.sort_index())
print(ser.sort_values())
print("--------------------")
print(df2)
print(df2.B)
print(df2.C)


df = pd.DataFrame(np.arange(9).reshape(3, 3),   columns=['A', 'B', 'C'])
print(df)
df.loc[:, 'D'] = df.loc[:, 'A']
df.loc[3, :] = df.loc[2, :]
print(df)
print("-----------------------")
df3 = df1 - df2
print(df3)
print(df3.fillna(method='ffill'))
print(df3.loc[:,"B":"C"].dropna(axis=1))
print(df3.replace(np.nan,1.0))