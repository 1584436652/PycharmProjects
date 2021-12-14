import requests
from lxml import etree
from xpinyin import Pinyin
import pypinyin

def write(filePath):
    with open('C:\\Users\\Administrator\\Desktop\\a.txt', 'w', encoding='utf8') as fp:
        for i in filePath:
            for j in i:
                print(j)
                fp.write(j + '\n')


def read(filePath):
    with open(filePath, 'r', encoding='utf-8')as fp:
        r = fp.read()
        print(r)
        return r


def get_data():
    choose = input("输入名句类型:")
    se = ''
    for ye in pypinyin.pinyin(choose, style=pypinyin.NORMAL):
        se += ''.join(ye)
    print(se)
    url = 'https://www.lz13.cn/' + se + '/71085.html'
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
        'content-type': 'text/html'
    }

    respones = requests.get(url=url, headers=headers)
    respones.encoding = respones.apparent_encoding  # 设置解码方式
    res = respones.text  # 解码
    # print(res)
    html = etree.HTML(res)
    html_text = html.xpath('//*[@id="node-8890"]/div[2]')
    for i in html_text:
        famous_quotation = i.xpath('./p/text()')
        # for j in a:
        #      item.append(j)
    return famous_quotation


write([get_data()])

# write(get_data())
# filePath = r'C:\\Users\\Administrator\\Desktop\\a.txt'
# write(read(filePath))






