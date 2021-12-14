from openpyxl import load_workbook
import pymysql


config = {
	'host': '127.0.0.1',
	'port':3306,
	'user': 'root',
	'password': 'root',
	'charset': 'utf8mb4',
	# 'cursorclass': pymysql.cursors.DictCursor
}
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()
name = 'lyexcel'
cursor.execute('create database if not exists %s' %name)
conn.select_db(name)
table_name = 'work'
cursor.execute('create table if not exists %s(id MEDIUMINT NOT NULL AUTO_INCREMENT,MerchantOrderID varchar(200),CustomerEmail varchar(200),primary key (id))'%table_name)

wb2 = load_workbook('C:\\Users\Administrator\Desktop\Work_Demo.xlsx')
# ws=wb2.get_sheet_names()
# print(ws)
for row in wb2:
    print("1")
    for cell in row:
        value1=(cell[0].value,cell[1].value)
        print(value1)
        cursor.execute('insert into work (MerchantOrderID,CustomerEmail) values(%s,%s)', value1)
        # sql = u"insert into work (PKID,MerchantSitePKID,GatewaySitePKID,MerchantOrderID) values (%s,%s,%s,%s)"
        # cursor.executemany(sql,value1)
        # conn.commit()

print("overing...")