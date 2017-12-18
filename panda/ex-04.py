"""
將資料寫入 Excel 檔案
"""
import pandas as pd

file = 'sample-04.xlsx'
path = '../data/'
file_path = path + file
# print('file_path = {}'.format(file_path))

# Load file
wb = pd.ExcelFile(file_path)

# load a sheet into a DataFrame
df = wb.parse('工作表1')

# write to excel file
writer = pd.ExcelWriter('../out/ex-04.xlsx', engine='xlsxwriter')
df.to_excel(writer, 'Sheet2')
writer.save()

# write to csv file
df.to_csv('../out/ex-04.csv')