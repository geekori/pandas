# 查看数据集中的列
import pandas
df = pandas.read_csv('../gapminder.tsv',sep='\t')

# 获取列
country_df = df['country']
#print(country_df)
print(country_df.head())
print(country_df.tail())
print(country_df.tail(20))

subset = df[['country', 'continent', 'year']]
print(subset.head())
print(subset.tail())