from lxml import etree
import xlwt
import requests
import json


url = 'http://hl.anseo.cn/rate_USD.aspx?'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
     # "Referer": "https://fanyi.baidu.com/?aldtype=16047",
}
respones = requests.get(url = url,headers = headers).text
html = etree.HTML(respones)
data = []
st = html.xpath('//*[@id="rates"]/ul/li')
for i in st:
     a = i.xpath('./text()[1]')
     b = i.xpath('./text()[2]')[0][1:4]
     c = i.xpath("./a/text()")
     r = list(b)
     title = c + a + r
     data.append(title)
d = ['美元', '1 美元 = 1.00 ', 'U', 'S', 'D']
data.append(d)


print(data)

myxls = xlwt.Workbook()
sheet1 = myxls.add_sheet(u'top250', cell_overwrite_ok=True)
for i in range(0, len(data)):
     sheet1.write(i, 0, i + 1)
     sheet1.write(i, 1, data[i])
myxls.save('D:\\汇率.xls')