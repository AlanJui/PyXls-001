"""
範例：
（１）在目錄中切換
（２）條列現行目錄中所有檔案
"""
# import os
import os

# retrieve current working directory (cwd)
cwd = os.getcwd()
cwd

# change directory
# os.chdir("/d/Workspace/PythonExcel/PyXls-001")
os.chdir("D:\\Workspace\\PythonExcel\\PyXls-001\\data")

# list all files and directories in current directory
os.listdir('.')
print(os.listdir('.'))