# Series的向量操作
import pandas as pd
scientists = pd.read_csv('../scientists.csv')

ages = scientists['Age']
print(ages)
print(ages + ages)
print(ages * ages)
print(ages + 100)
print(ages * 3)

print(ages + pd.Series([1,100]))

import numpy as np
#print(ages + np.array([1,2,3,4,5]))
print(ages + np.array([1,2,3,4,5,6,7,8]))