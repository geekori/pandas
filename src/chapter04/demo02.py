# 数据遗失的原因

import pandas as pd
# 装载数据
visited_file = '../data/survey_visited.csv'

print(pd.read_csv(visited_file))
print(pd.read_csv(visited_file,na_values=[' '],keep_default_na=False))

# 合并数据
visited = pd.read_csv('../data/survey_visited.csv')
survey = pd.read_csv('../data/survey_survey.csv')
vs = visited.merge(survey,left_on='ident',right_on='taken')
print(vs)

# 用户输入
scientists = pd.DataFrame({
    'Name':['Bill','Mike'],
    'Occupation':['Chemist','Statistician']    
    })
print(scientists)
from numpy import nan
scientists['missing'] = nan
print(scientists)

# 重建索引
gapminder = pd.read_csv('../data/gapminder.tsv',sep='\t')
life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
print(life_exp)
print(life_exp.loc[range(2000,2003)])
