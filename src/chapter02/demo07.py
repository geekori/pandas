# DataFrame的过滤条件
import pandas as pd
scientists = pd.read_csv('../scientists.csv')

print(scientists)

print(scientists[scientists['Age'] > scientists['Age'].mean()])
print(scientists.loc[[True,True,False,True]])
print(scientists.iloc[[1,3,4]])

print(scientists[['Name','Age','Occupation']][scientists['Age'] > scientists['Age'].mean()])

print(scientists[['Name','Age','Occupation']][scientists['Age'] > scientists['Age'].mean()].loc[[True,True]])

print(scientists[['Name','Age','Occupation']][scientists['Age'] > scientists['Age'].mean()].iloc[[0,2]])
