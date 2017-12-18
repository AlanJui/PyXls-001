"""
自 CSV 檔案讀入資料
"""
import pandas as pd

file = 'sample.csv'
path = '../data/' + file
print(path)

# Load file
df = pd.read_csv(path)
print(df)