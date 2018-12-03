# 删除DataFrame中的列

import pandas as pd
scientists = pd.read_csv('../scientists.csv')
print(scientists.columns)

scientists_dropped = scientists.drop(['Age','Died'],axis = 1)
print(scientists_dropped.columns)
print(scientists_dropped)