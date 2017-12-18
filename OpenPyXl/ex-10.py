"""
Reading and Formatting Excel Files: xlrd
"""
import xlrd

# Load Excel file data into DataFrame
file = 'sample.xlsx'
dir_path = '../data/'
file_path = dir_path + file
# print(file_path)

#========================================
# Load workbook
#========================================

# open a workbook
wb = xlrd.open_workbook(file_path)

# loads only current sheets to memory
wb1 = xlrd.open_workbook(file_path, on_demand=True)

#========================================
# Load a sheet
#========================================

# load a specific sheet by name
ws = wb.sheet_by_name('工作表1')

# load a specific sheet by index
ws1 = wb1.sheet_by_index(0)

#========================================
# retrieve value from cell
#========================================

data = ws.cell(0, 0).value
print('data = {}'.format(data))
