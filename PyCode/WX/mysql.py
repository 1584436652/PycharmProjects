import pymysql
db = pymysql.connect(
   host="localhost",  # 主机名
   user="root",     # 用户名
   passwd="root", # 密码
   db="demo")    # 数据库名称
# 查询前，必须先获取游标
cur = db.cursor()
# 执行的都是原生SQL语句
cur.execute("SELECT * FROM lkt")
for row in cur.fetchall():
  print(row)
db.close()