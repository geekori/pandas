# 直接修改DataFrame中列的值
import pandas as pd
scientists = pd.read_csv('../scientists.csv')
import random
ageList = [random.randint(30,100) for i in range(8)]
scientists['Age'] = ageList

print(scientists['Age'])
