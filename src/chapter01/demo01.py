# 装载数据集
# country（国家）  continent（洲） year（年份）  
# lifeExp（预期寿命）  pop（人口）    gdpPercap（人均GDP）

import pandas
df = pandas.read_csv('../gapminder.tsv',sep='\t')
print(type(df))
# 获取前面的n行
print(df.head())
print(df.head(10))
print(type(df.head()))

# 获取二维表的维度
print(df.shape)
print(df.shape[0])
print(df.shape[1])

# 获取列名
print(df.columns)
for column in df.columns:
    print(column)

print(df.dtypes)
for type in df.dtypes:
    print(type)
print('-----------')
columnTypes = dict(zip(df.columns,df.dtypes))
print(columnTypes.get('country'))
print(columnTypes.get('pop'))

print(df.info())

'''
object        string
int64         int
float64       float 
datetime64    datetime
'''
