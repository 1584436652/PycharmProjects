import requests
from lxml import etree
import os
import openpyxl as xl
import pymysql


# db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='test', port=3306, charset='utf8')
# print("MySQL连接成功")
# table_name = 'exchange_rate'
# conn = db.cursor()
# conn.execute('create table if not exists %s(id MEDIUMINT NOT NULL AUTO_INCREMENT,name varchar(200),primary key (id))'%table_name)
bizhong = input("输入币种 如（CNY）：")
url = "https://m.huilv.cc/curreny_list.html?"
parems = {
       "from":bizhong,
        "to":""
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}
response = requests.get(url=url, headers=headers,params=parems)
html = response.text
html_data = etree.HTML(html)
# print(html)
res = html_data.xpath('//*[@class="table_box"]')
# print(res)
for i in res:
    a = i.xpath("./div[1]/ul/li/a/span[1]/text()")
    b = i.xpath("./div[1]/ul/li/a/span[2]/text()")
    c = i.xpath('./div[2]/div[1]/ul/li[2]/ul[@class="list"]/li[1]/text()')
    d = i.xpath('./div[2]/div[1]/ul/li[2]/ul[@class="list"]/li[2]/text()')
    data1 = [a, b, c, d]
    print(data1)


def write_excel_file(folder_path):
    result_path = os.path.join(folder_path, "新汇率网址.xlsx")
    print(result_path)
    print('***** 开始写入excel文件 ' + result_path + ' ***** \n')
    # if os.path.exists(result_path):
    #     print('***** excel已存在，在表后添加数据 ' + result_path + ' ***** \n')
    #     workbook = xl.workbook(result_path)
    # else:
    #     print('***** excel不存在，创建excel ' + result_path + ' ***** \n')
    workbook = xl.Workbook()
    workbook.save(result_path)
    sheet = workbook.active
    header = ["名称","A","B","C"]
    sheet.append(header)
    result = data1
    for data in result:
        sheet.append(data)
    workbook.save(result_path)
    print('***** 生成Excel文件 ' + result_path + ' ***** \n')


if __name__ == '__main__':
    write_excel_file("D:\\")