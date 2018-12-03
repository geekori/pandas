# 清除非值数据

# 1. 填充NaN
# 2. 删除包含NaN的行

import pandas as pd
gapminder = pd.read_csv('../data/gapminder.tsv',sep='\t')
life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
a = life_exp.loc[range(2000,2010)]
print(a)
print(a.fillna(0))
print(a.fillna('*'))

# forward填充（用前面的值填充当前的NaN）
print(a.fillna(method='ffill'))

# backward填充（用后面的值填充当前的NaN）
print(a.fillna(method='bfill'))

print(a.fillna(method='bfill').fillna(method='ffill'))

print(a.interpolate())
from numpy import NaN
aa = pd.Series([NaN,NaN,2,NaN,4,NaN,6,NaN,NaN,9,NaN,NaN,NaN])
print(aa.interpolate())

# 删除包含NaN的行
print(aa.dropna())