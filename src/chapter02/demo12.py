# 读写Pickle格式的Series和DataFrame文件

import pandas as pd
scientists = pd.read_csv('../scientists.csv')
names = scientists['Name']
print(names)

import os

if not os.path.exists('./output/scientists_names_series.pickle'):
    names.to_pickle('./output/scientists_names_series.pickle')
if not os.path.exists('./output/scientists_df.pickle'):
    scientists.to_pickle('./output/scientists_df.pickle')

# 读取Pickle文件
scientists_names_from_pickle = pd.read_pickle('./output/scientists_names_series.pickle')
print(scientists_names_from_pickle)

scientists_from_pickle = pd.read_pickle('./output/scientists_df.pickle')
print(scientists_from_pickle)
