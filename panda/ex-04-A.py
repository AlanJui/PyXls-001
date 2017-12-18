"""
將資料寫入 Excel 檔案
"""
import pandas as pd
from openpyxl import load_workbook

file = 'sample-04.xlsx'
path = '../data/'
file_path = path + file
# print('file_path = {}'.format(file_path))

# Load file
wb = load_workbook(file_path)

# 依「工作表的名稱」取得工作表
sheet = wb.get_sheet_by_name('工作表1')

# write to excel file
writer = pd.ExcelWriter('../out/ex-04-A.xlsx', engine='openpyxl')
writer.book = wb
writer.sheets = sheet
writer.save()

