# 查看数据集中的行
import pandas
df = pandas.read_csv('../gapminder.tsv',sep='\t')

# loc   iloc
print(df.loc[0])
print(df.loc[15])
# print(df.loc[-1])  error
number_of_rows = df.shape[0]
print(df.loc[number_of_rows - 1])
print(type(df.loc[number_of_rows - 1]))
print(type(df.head()))

print('---------')
print(df.loc[[2,4,5]])
print(df.iloc[-1])



