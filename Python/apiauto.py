import json
import xml
import requests
import oauthlib.oauth1
import time
cKey = "NFEOCBUT"
sKey = "FLIATMXBJEAAP2E7EPTDVI2A"
MerchantId = '4459800d-10f4-4d50-8ecd-db626aabbb12'
api_url_base = 'http://www.testln.martjack.com/devapi/'
import openpyxl
import os
os.getcwd()
os.chdir('E:/')
wb = openpyxl.load_workbook('ApiAuto.xlsx')
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet1')

i = 0
for i in range (0,3):
    i = i + 1
    sheet['A'+str(i)].value
    print(sheet['A'+str(i)].value) 
    url= api_url_base+sheet['A'+str(i)].value+ MerchantId
    print(url)
    
   # response = requests.post(uri, headers =headers , data=payload)
  