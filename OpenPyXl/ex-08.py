import pandas as pd
from openpyxl import load_workbook
import itertools

# Load Excel file data into DataFrame
file = 'sample.xlsx'
dir_path = '../data/'
file_path = dir_path + file
# print(file_path)

# 載入 Excel 檔案（即：活頁簿）
wb = load_workbook(file_path)

# 依「工作表的名稱」取得工作表
sheet = wb.get_sheet_by_name('工作表1')

#========================================

# put the sheet values in 'data'
data = sheet.values
print('data = {}'.format(data))

# indicate the columns in the sheet values
# get the header of data in sheet
cols = next(data)[1:]
print('cols = {}'.format(cols))

# convert your data to a list
# get product name list
data_list = list(data)
print('data = {}'.format(data_list))

# Read in the data at index 0 (ID of row data) for the indices
idx = [row[0] for row in data_list]
print('idx = {}'.format(idx))

# # for loop to get a row
# for row in data_list:
#     print('row = {}'.format(row))

# Slice the data at index 1
data_without_idx = (itertools.islice(row, 1, None) for row in data_list)
# print('data_without_idx = {}'.format(data_without_idx))

# make your DataFrame
df = pd.DataFrame(data_without_idx, index=idx, columns=cols)
print('df = {}'.format(df))

