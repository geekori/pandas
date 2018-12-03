# Series的条件过滤
import pandas
scientists = pandas.read_csv('../scientists.csv')
ages = scientists['Age']
print(ages)
print(ages.describe())
print(ages[ages > ages.mean()])
print(ages > ages.mean())
print(type(ages > ages.mean()))
print(ages[[True,True,False,True,False,True,True,False]])