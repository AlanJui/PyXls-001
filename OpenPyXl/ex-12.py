"""
Writing Your Data to Excel Files with xlwt
"""

import xlwt

#========================================
# Load workbook
#========================================

# Initialize a workbook
wb = xlwt.Workbook()

# add a sheet to the workbook
ws = wb.add_sheet('Sheet1')

# the data
cols = ['A', 'B', 'C', 'D', 'E']
txt = [0, 1, 2, 3, 4]

# loop over the rows and columns and fill in the values
for num in range(5):
    row = ws.row(num)
    for index, col in enumerate(cols):
        value = txt[ index ] + num
        row.write(index, value)

# save the result
wb.save('../out/wb2.xls')

