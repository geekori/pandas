# Series中的方法
import pandas as pd
import matplotlib.pyplot as plt
scientists = pd.DataFrame({
    'Name':['Rosaline Franklin', 'William Gosset'],
    'Occupation':['Chemist', 'Statistician'],
    'Born':['1920-07-25', '1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]},columns=['Occupation','Born','Died','Age'],
            index=['Rosaline Franklin', 'William Gosset'])
print(scientists)

ages = scientists['Age']
print(type(ages))
print(ages)
print(ages.mean())  # 取平均数
print(ages.min())
print(ages.max())
print(ages.std())
print(ages.sort_values(ascending=False))
print(ages.append(ages))

ages.hist()
plt.show()