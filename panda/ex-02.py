"""
自 Excel 檔案，讀入資料：
（１）顯示工作表名稱
（２）依工作表名稱，將資料讀入 DataFrame
"""
import pandas as pd

file = 'sample.xlsx'
path = '../data/' + file
print(path)

# Load file
xlsx = pd.ExcelFile(path)

# display all the sheet name
print(xlsx.sheet_names)

# load a sheet into a DataFrame by name: df1
df1 = xlsx.parse('工作表1')
print(df1)
