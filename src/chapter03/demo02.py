# 连接与合并数据集：列连接

import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

col_concat = pd.concat([df1,df2,df3],axis = 1)

print(col_concat)
print(col_concat['B'])

# 添加一列
col_concat['new_col_list'] = ['n1','n2','n3','n4']
print(col_concat)

# 用Series添加一列
col_concat['new_col_series'] = pd.Series(['n1','n2','n3','n4'])
print(col_concat)

col_concat = pd.concat([df1,df2,df3],axis=1,ignore_index=True)
print(col_concat)
print(col_concat[2])  # 第3列
print(col_concat[2][1]) # 第3列第2行
print(col_concat[1:3])  # 第2行第3行
