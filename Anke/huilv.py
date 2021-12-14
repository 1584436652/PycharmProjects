import openpyxl as xl
import os
from lxml import etree
import requests



url = 'http://hl.anseo.cn/rate_USD.aspx?'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
     # "Referer": "https://fanyi.baidu.com/?aldtype=16047",
}
respones = requests.get(url = url,headers = headers).text
html = etree.HTML(respones)
data1 = []
st = html.xpath('//*[@id="rates"]/ul/li')
for i in st:
     a = i.xpath('./text()[1]')
     b = i.xpath('./text()[2]')[0][1:4]
     c = i.xpath("./a/text()")
     r = list(b)
     title = c + a + r
     data1.append(title)
d = ['美元', '1 美元 = 1.00 ', 'U', 'S', 'D']
data1.append(d)


print(data1)


def write_excel_file(folder_path):
    result_path = os.path.join(folder_path, "汇率.xlsx")
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
    headers = ["名称", "系数（美元）","A","B","C"]
    sheet.append(headers)
    result = data1
    for data in result:
        sheet.append(data)
    workbook.save(result_path)
    print('***** 生成Excel文件 ' + result_path + ' ***** \n')

if __name__ == '__main__':
    write_excel_file("D:\\")

