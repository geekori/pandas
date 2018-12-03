# 读写Excel格式的Series和DataFrame文件

import pandas as pd
scientists = pd.read_csv('../scientists.csv')
names = scientists['Name']
#print(names)

names.to_excel('./output/scientists_names_series.xls')
names_df = names.to_frame()
names_df.to_excel('./output/scientists_names_series1.xls')

scientists.to_excel('./output/scientists_df.xlsx',sheet_name='scientists', index = False)

import xlrd
#  workbook   sheet

data = xlrd.open_workbook('./output/scientists_df.xlsx')
sheet = data.sheet_by_name('scientists')
sheet = data.sheet_by_index(0)
print(sheet.row_values(1))
print(sheet.col_values(1))
print('行数','=',sheet.nrows)
print('列数','=',sheet.ncols)

print(sheet.cell(0,0).value)
print(sheet.cell(2,3).value)

print(data.sheet_names())

print(sheet.name)

print(sheet.row_values(3))
print(sheet.col_values(2))

