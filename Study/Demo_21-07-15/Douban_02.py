import requests
import json
from urllib.parse import urlencode
import pymysql


# 连接MYSQL数据库
db = pymysql.connect(host='127.0.0.1',user='root',password='root',db='test',port=3306,charset='utf8')
print('连接数据库成功！')
conn = db.cursor() # 获取指针以操作数据库
conn.execute('set names utf8')
table_name = 'Douban_mysql'
conn.execute('create table if not exists %s(id MEDIUMINT NOT NULL AUTO_INCREMENT,title varchar(200)NOT NULL,rate varchar(200),url varchar(200),primary key (id,title))'%table_name)

leixing = input("选电影(热门/最新...):")
#  请求地址

#  请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
    'Cookie': 'viewed="1398395"; bid=-IbSUPgbDCI; gr_user_id=0cb6873d-d518-4e56-a030-09140761398e; __gads=ID=ab98dbfdc94408cb-2285c4c563c900ef:T=1623466156:RT=1623466156:S=ALNI_MY2bEMOGY81zvyP-Qer_mk1wriosg; douban-fav-remind=1; ll="118282"; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=D2EDA3C6A603CD27EC905CB686C389165|d1abed604eabf8daaccf97b4c2c9e22e; __utmz=30149280.1626320262.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1626320262.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1626326519%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhJyVtaouuSLKVh6BvcRskflvIVg8oEQm92CxjQBrvGu7V7culbE05BzJte2Spjd4%26wd%3D%26eqid%3Dc31a0ac0000099ae0000000660efad86%22%5D; _pk_id.100001.4cf6=55e297afd29ce5f5.1626317085.3.1626326519.1626320262.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1305676726.1623466153.1626320262.1626326519.5; __utmb=30149280.0.10.1626326519; __utma=223695111.1037641943.1626317085.1626320262.1626326519.3; __utmb=223695111.0.10.1626326519'
}
# 携带的参数sort=time&page_limit=20&page_start=0
# print(url)
for i in range(0,10):
    count = i * 20
    parm = {
        'type': 'movie',
        'tag': leixing,
        'sort': 'recommend',
        'page_limit': 20,
        'page_start': count,
    }
    url = "https://movie.douban.com/j/search_subjects?"
    # 拼接请求参数
    ajax_url = url
    # 发送请求
    data_json = requests.get(ajax_url, headers=headers,params=parm).json()
    # print(data_json)

    for i in data_json['subjects']:
        title = i['title'],
        rate = i['rate'],
        url = i['url'],
        douban = [title,rate,url]
        sql = u"INSERT IGNORE INTO Douban_mysql(title,rate,url) VALUES(%s,%s,%s)"
        conn.execute(sql,douban)
        conn.execute('delete from douban_mysql where id not in (select t.max_id from (select max(id) as max_id from douban_mysql group by title,rate,url) as t)')
        db.commit()  # 提交操作
        print('插入数据成功!')

# 关闭MySQL连接
conn.close()
db.close()


