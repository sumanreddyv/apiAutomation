import requests
import oauthlib
import pymysql

host = '10.16.3.10'
user = 'technobahn'
password = 'willy007'
database = 'martjack'

db = pymysql.connect(host=host,user=user, passwd=password, database=database)

c = db.cursor()

c.execute("select * from tblbusinessruleperiodicity  where RuleId = '30066'")

results = c.fetchall()

for row in results:
    print(row) 