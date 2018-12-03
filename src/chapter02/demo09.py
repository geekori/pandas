# 向DataFrame添加列
import pandas as pd
scientists = pd.read_csv('../scientists.csv')
print(scientists['Born'].dtype)
print(scientists['Died'].dtype)

born_datetime = pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'],format='%Y-%m-%d')

scientists['born_dt'],scientists['died_dt'] = (born_datetime,died_datetime)
print(scientists.head())
print(scientists['born_dt'].dtype)

print(scientists.shape)

