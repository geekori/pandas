# 创建DataFrame
import pandas as pd
"""
scientists = pd.DataFrame({
    'Name':['Rosaline Franklin', 'William Gosset'],
    'Occupation':['Chemist', 'Statistician'],
    'Born':['1920-07-25', '1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]},columns=['Occupation','Born','Died','Age'],
            index=['Rosaline Franklin', 'William Gosset']
                          )
print(scientists)
"""

# 使用有顺序的字典
from collections import OrderedDict
scientists = pd.DataFrame(OrderedDict([
    ('Name',['Rosaline Franklin', 'William Gosset']),
    ('Occupation',['Chemist', 'Statistician']),
    ('Born',['1920-07-25', '1876-06-13']),
    ('Died',['1958-04-16','1937-10-16']),
    ('Age',[37,61])
    ]))
print(scientists)

