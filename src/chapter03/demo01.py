# 连接与合并数据集：行连接

import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')
print(df1)
print(df2)
print(df3)

row_concat = pd.concat([df1,df2,df3])
# union all
print(row_concat)
print(row_concat.iloc[4,])
print(row_concat.iloc[4:6,])

new_row_series = pd.Series(['n1','n2','n3','n4'])
print(new_row_series)

print(pd.concat([df1,new_row_series]))

new_row_df = pd.DataFrame([['n1','n2','n3','n4']],
                          columns=['A','B','C','D'])
print(new_row_df)
print(pd.concat([df1,new_row_df]))
print(pd.concat([df1,new_row_df],ignore_index=True))
