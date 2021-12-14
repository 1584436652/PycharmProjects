import os,sys
import requests
import bs4
import pymysql


# 连接MYSQL数据库
db = pymysql.connect(host='127.0.0.1',user='root',password='root',db='test',port=3306,charset='utf8')
# db = MySQLdb.connect('127.0.0.1','root','mysql','test',coon.set_character_set('utf8'))
print('连接数据库成功！')
conn = db.cursor() # 获取指针以操作数据库
conn.execute('set names utf8')


html = 'https://www.dongmanmanhua.cn/dailySchedule?weekday=MONDAY'
result = requests.get(html)
texts = result.text
data = bs4.BeautifulSoup(texts,'html.parser');
lidata = data.select('div#dailyList ul.daily_card li')
# print(lidata)
arr = {}

for x in lidata:
    did = x.get('data-title-no')
    print(did)
    name = x.select('p.subj')
    name1 = name[0].get_text()
    url = x.a.get('href')
    # print(url)
    story = x.a.p
    story1 = story.string
    user = x.select('p.author')
    user1 = user[0].get_text()
    like = x.select('em.grade_num')
    like1 = like[0].get_text()

    # 写入MYSQL数据库
    t = [did,name1,url,story1,user1,like1]
    sql = u"INSERT INTO dongman(did,name,url,story,user,likes) VALUES(%s,%s,%s,%s,%s,%s)"
    conn.execute(sql,t)

#    t1 = (did,name1,url,story1,user1,like1)
#    sql1 = u'''insert into dongman(did,name,url,story,user,likes) values (%d,'%s','%s','%s','%s','%s')''' % t1
#    conn.execute(sql1)
    db.commit()  # 提交操作
    print('插入数据成功!')


#关闭MySQL连接
conn.close()
db.close()