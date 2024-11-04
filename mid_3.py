import pandas as pd
import numpy as np

df1_data = np.ones((6, 7))
df1 = pd.DataFrame(df1_data, index=list('abcdef'), columns=list('ABCDEFG'))
df2_data = np.ones((7, 6))
df2 = pd.DataFrame(df2_data, index=list('abcdefg'), columns=list('ABCDEF'))
df3=df1+df2

df3[:] = np.nan
df3.loc[['a', 'b', 'c', 'f'], ['A', 'B', 'C', 'D', 'E', 'F']] = [[np.nan, 3, 3, np.nan, np.nan, 2], [3, 3, 3, np.nan, np.nan, 2], [3, 3, 3, np.nan, np.nan, 2], [2, 2, 2, 2, 2, 2]]
df3.loc[['d', 'e'], ['F']] = 2
print(df3)














