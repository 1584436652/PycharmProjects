import requests
from lxml import etree
import pymysql
import cv2
from xpinyin import Pinyin


db = pymysql.connect(host='127.0.0.1',user='root',password='root',db='test',charset='utf8mb4',port=3306)
print("连接数据库成功")
conn = db.cursor()
conn.execute('set names utf8')
table_name = 'baidu_picture'
conn.execute('create table if not exists %s(id MEDIUMINT NOT NULL AUTO_INCREMENT,img MEDIUMBLOB NOT NULL,primary key (id))'%table_name)
word = input('请输入要爬取的关键字：')
page = input('请输入要爬取多少页：')
page = int(page) + 1
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
n = 0
pn = 1
# pn是从第几张图片获取 百度图片下滑时默认一次性显示30张
for m in range(1, page):
    url = 'https://image.baidu.com/search/acjson?'

    param = {
        'tn': 'resultjson_com',
        'logid': '',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': word,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': word,
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'cg': 'girl',
        'pn': pn,  # 从第几张图片开始
        'rn': '30',
        'gsm': '1e',
    }
    page_text = requests.get(url=url, headers=header, params=param)
    page_text.encoding = 'utf-8'
    page_text = page_text.json()
    info_list = page_text['data']
    del info_list[-1]
    img_path_list = []
    for i in info_list:
        img_path_list.append(i['thumbURL'])

    for img_path in img_path_list:
        img_data = requests.get(url=img_path, headers=header)
        img_path = './' + str(n) + '.jpg'
        print(img_path)
        # with open(img_path, 'wb') as fp:
        #     fp.read(img_path)
        a = cv2.imread(img_path)
        print(a)
        baidu_pic = [a]
        # conn.execute("INSERT INTO baidu_picture SET Data= %s" % pymysql.Binary(img_path))
        sql = u"INSERT IGNORE INTO baidu_picture(id,img) VALUES(null,%s)"
        conn.execute(sql, baidu_pic)
        db.commit()


        n = n + 1

    pn += 29
# 关闭MySQL连接
conn.close()
db.close()
