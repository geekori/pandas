# 读写CSV格式的Series和DataFrame文件

import pandas as pd
scientists = pd.read_csv('../scientists.csv')
names = scientists['Name']
print(names)

import os
if not os.path.exists('./output/scientists_names_series.csv'):
    names.to_csv('./output/scientists_names_series.csv')
if not os.path.exists('./output/scientists_names_series1.csv'):
    names.to_csv('./output/scientists_names_series1.csv',sep='*')
if not os.path.exists('./output/scientists_names_series2.csv'):
    names.to_csv('./output/scientists_names_series2.csv',index=False)

if not os.path.exists('./output/scientists_df1.csv'):
    scientists.to_csv('./output/scientists_df1.csv')
if not os.path.exists('./output/scientists_df2.csv'):
    scientists.to_csv('./output/scientists_df2.csv',index=False)
    