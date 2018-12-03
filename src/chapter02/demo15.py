# 将Series和DataFrame导出为其他格式（json、html、sqlite等）的数据

import pandas as pd
scientists = pd.read_csv('../scientists.csv')
scientists.to_clipboard()

#print(scientists.to_dict())
print(scientists.to_html())
scientists.to_json('./output/scientists.json')

import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///my_db.sqlite')
scientists.to_sql('scientists',engine,if_exists = 'append')
