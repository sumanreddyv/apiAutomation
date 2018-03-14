import openpyxl
import os
os.getcwd()
os.chdir('C:/Users/suman.venkanolla/Documents/GitHub/apiAutomation/Python')
wb = openpyxl.load_workbook('GetALlPromotions.xlsx')
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet3')
#print(sheet['A1'].value)
payload= sheet['A1'].value
print(payload)

