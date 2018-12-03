# 查看数据集中的单元格
import pandas
df = pandas.read_csv('../gapminder.tsv',sep='\t')

# loc和iloc

subset = df.loc[:,['year', 'pop']]
print(subset.head())

subset = df.iloc[:,[2,4,-1]]
print(subset.head())

# 分片
subset = df.iloc[:,3:6]
print(subset.head())
subset = df.iloc[0:3,3:6]
print(subset)

subset = df.loc[1,'lifeExp']
print(subset)
subset = df.loc[1:5,['year', 'pop']]
print(subset)

subset = df.iloc[[1,3,5],[0,2,3]]
print(subset)







