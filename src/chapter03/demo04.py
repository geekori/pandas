# 合并多个数据集

# 合并：关系型数据库中的两个表之间的连接
# table1.field1   table2.field2
# select table1.field1,table2.field2 from table1,table2
# where table1.field1 = table2.field2
# 1.  一对一
# 2. 多对一
# 3. 多对多

import pandas as pd

person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')

print(person)
print(site)
print(visited)
print(survey)

visited_subset = visited.loc[[0,2,6],]
print(visited_subset)

# 一对一连接
merge1 = site.merge(visited_subset,left_on='name',right_on='site')
print(merge1)

# 多对一
merge2 = site.merge(visited,left_on='name',right_on='site')
print(merge2)

# 多对多
ps = person.merge(survey,left_on='ident',right_on='person')
vs = visited.merge(survey,left_on='ident', right_on='taken')
print(ps)
print(vs)


