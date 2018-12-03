#非值数据：Pandas中有哪些非值数据
import pandas as pd
from numpy import NaN,NAN,nan
# NaN 

# NaN是被遗失的数据
print(NaN == True)
print(NaN == False)
print(NaN == 0)
print(NaN == '')

print(NaN == NaN)
print(NaN == nan)
print(NaN == NAN)

x = NaN
y = NAN
n = 20
print(pd.isnull(x))
print(pd.isnull(y))
print(pd.notnull(n))
