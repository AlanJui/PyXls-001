"""
Writing Your Data to Exc el Files with xlwt
"""

import xlwt

#========================================
# Load workbook
#========================================

# Initialize a workbook
wb = xlwt.Workbook(encoding='utf-8')

# add a sheet to the workbook
ws1 = wb.add_sheet('Python Sheet1')

# write to the sheet of the workbook
ws1.write(0, 0, 'This is the First Cell of the First Sheet')

# save the workbook
wb.save('../out/wb1.xls')

