
import json
import xml
import requests
import oauthlib.oauth1
import time
cKey = "NFEOCBUT"
sKey = "FLIATMXBJEAAP2E7EPTDVI2A"
MerchantId = '4459800d-10f4-4d50-8ecd-db626aabbb12'
api_url_base = 'http://www.testln.martjack.com/devapi/' 
url= api_url_base+'Carts/GetAllPromotions/'+ MerchantId
headers = {'Content-type': 'application/json' }
client = oauthlib.oauth1.Client(client_key=cKey, client_secret=sKey, signature_method=oauthlib.oauth1.SIGNATURE_HMAC, signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY, timestamp= time.time())

uri, header, body = client.sign(url, http_method='POST')

import openpyxl
import os
import xlsxwriter
import xlrd
#import getpass
os.getcwd()
os.chdir('E:/')
wb = openpyxl.load_workbook('GetALlPromotions.xlsx')
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet3')


i = 0
for i in range (0,3):
    i = i + 1
    sheet['A'+str(i)].value
    print(sheet['A'+str(i)].value) 
    payload= sheet['A'+str(i)].value
    response = requests.post(uri, headers =headers , data=payload)
    print(response.text)
    for j in range (0,3):
        j = i + 1
        sheet['B'+str(i)].value = response.text
wb.save('GetALlPromotions.xlsx')
#print(sheet['A1'].value)


"""payload= {
      "locationcode": "",
  "deliverymode": "",
  "channeltype": "",
  "promotiontype": "cart",
  "hasvouchers": "",
  "fromdate": "2018-03-18",
  "fromtime": "13:00:00",
  "todate": "2018-03-31",
  "totime": "15:00:00",
  "activestatus": "true"
}"""
#data = json.dumps(payload)




#sheet['B2'].value = response.text
#wb.save('GetALlPromotions.xlsx')