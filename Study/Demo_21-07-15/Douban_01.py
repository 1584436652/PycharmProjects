import requests
import json
import string
import urllib.parse
from urllib.parse import urlencode
from bs4 import BeautifulSoup


def douban(name, count):
    #  请求地址
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&"
    #  请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
        'Cookie': 'viewed="1398395"; bid=-IbSUPgbDCI; gr_user_id=0cb6873d-d518-4e56-a030-09140761398e; __gads=ID=ab98dbfdc94408cb-2285c4c563c900ef:T=1623466156:RT=1623466156:S=ALNI_MY2bEMOGY81zvyP-Qer_mk1wriosg; douban-fav-remind=1; ll="118282"; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=D2EDA3C6A603CD27EC905CB686C389165|d1abed604eabf8daaccf97b4c2c9e22e; __utmz=30149280.1626320262.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1626320262.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1626326519%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhJyVtaouuSLKVh6BvcRskflvIVg8oEQm92CxjQBrvGu7V7culbE05BzJte2Spjd4%26wd%3D%26eqid%3Dc31a0ac0000099ae0000000660efad86%22%5D; _pk_id.100001.4cf6=55e297afd29ce5f5.1626317085.3.1626326519.1626320262.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1305676726.1623466153.1626320262.1626326519.5; __utmb=30149280.0.10.1626326519; __utma=223695111.1037641943.1626317085.1626320262.1626326519.3; __utmb=223695111.0.10.1626326519'
    }
    # 携带的参数sort=time&page_limit=20&page_start=0
    parm = {
        'sort': 'recommend',
        'page_limit': 20,
        'page_start': count,
    }
    # 拼接请求参数
    ajax_url = url
    # 发送请求
    data_json = requests.get(ajax_url, headers=headers,params=parm).json()

    with open('.\豆瓣数据.txt', 'a') as output:
        for index, data in enumerate(data_json['subjects']):
            # 评分
            rate = data['rate']
            # 标题
            title = data['title']
            # 图片
            cover = data['cover']
            # 发送下一次请求
            data_ = requests.get(data['url'], headers=headers).content.decode()
            print("正在准备下文件写入：" + title)
            # 格式转换
            soupData = BeautifulSoup(data_, 'lxml')
            #  解析数据
            aa = soupData.find(class_='subjectwrap clearfix')
            info = aa.find(attrs={'id': 'info'})
            try:
                if (len(info.find_all(class_='pl')) == 10):
                    # 写入文件
                    output.write(ten(rate, title, cover, info) + "\n")
                    output.flush()
                if (len(info.find_all(class_='pl')) == 7):
                    # 写入文件
                    output.write(seven(rate, title, cover, info) + "\n")
                    output.flush()
                print("成功向文件写入：" + title)
            except Exception:
                print("格式解析异常：" + title)

        output.close()


def seven(rate, title, cover, info):
    # 导演
    directors = []
    for s in info.find_all(attrs={'rel': 'v:directedBy'}):
        directors.append(s.string)
    # 主演
    protagonists = []
    for s in info.find_all(attrs={'rel': 'v:starring'}):
        protagonists.append(s.string)
    # 类型
    types = []
    for s in info.find_all(attrs={'property': 'v:genre'}):
        types.append(s.string)
    # 解析 制片国家
    ProductsCountry = info.find_all(class_='pl')[3].next_sibling
    # 语言
    language = info.find_all(class_='pl')[4].next_sibling
    # 上映日期
    date = info.find(attrs={'property': 'v:initialReleaseDate'}).string
    # 片长
    runtime = info.find(attrs={'property': 'v:runtime'}).string
    # 将数据保存到集合中
    list = {'rate': rate, 'title': title, 'cover': cover, 'directors': directors, 'protagonists': protagonists,
            'types': types, 'ProductsCountry': ProductsCountry,
            'language': language, 'date': date, 'runtime': runtime}
    # 返回集合
    return json.dumps(list)
def ten(rate, title, cover, info):
    # 导演
    directors = []
    for s in info.find_all(attrs={'rel': 'v:directedBy'}):
        directors.append(s.string)
    # 主演
    protagonists = []
    for s in info.find_all(attrs={'rel': 'v:starring'}):
        protagonists.append(s.string)
    # 类型
    types = []
    for s in info.find_all(attrs={'property': 'v:genre'}):
        types.append(s.string)
        # 解析 制片国家
    ProductsCountry = info.find_all(class_='pl')[4].next_sibling
    # 语言
    language = info.find_all(class_='pl')[5].next_sibling
    # 上映日期
    date = info.find(attrs={'property': 'v:initialReleaseDate'}).string
    # 片长
    runtime = info.find(attrs={'property': 'v:runtime'}).string
    alternateName = info.find_all(class_='pl')[8].next_sibling
    # 将数据保存到集合中
    list = {'rate': rate, 'title': title, 'cover': cover, 'directors': directors, 'protagonists': protagonists,
            'types': types, 'ProductsCountry': ProductsCountry,
            'language': language, 'date': date, 'runtime': runtime, 'alternateName': alternateName}
    # 返回集合
    return json.dumps(list)


if __name__ == '__main__':
    name = urllib.parse.quote("热门", safe=string.ascii_letters)
    for i in range(0, 3):
        douban(name=name, count=i *20)