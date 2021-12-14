import pymysql
def export(table_name):
    conn =pymysql.connect(host = '127.0.0.1',
                           user = 'root',password='root',
                           db='test',port=3306,charset = 'utf8')
    print('连接数据库成功！')
    cur = conn.cursor()
    # cur.execute('select title from %s'%table_name)
    # cur.execute('delete from douban_mysql where id not in (select t.max_id from (select max(id) as max_id from douban_mysql group by title,rate,url) as t)')
    cur.execute('select img from %s where id = 48'%table_name )

    a = cur.fetchone()[0]
    b = open('./a.jpg','wb')
    b.write(a)
    b.close()
    cur.close()


    print(a)


export('baidu_picture')

