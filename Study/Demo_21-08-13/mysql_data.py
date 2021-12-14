import pymysql


class Connect_mysql(object):

    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = 'root'
        self.db = 'test'
        self.port = 3306
        self.charset = 'utf8'

    """连接数据库"""
    def get_connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, charset=
            self.charset, db=self.db)
            self.cursor = self.conn.cursor()
            print("mysql连接成功")
        except:
            print('mysql连接报错')

    # def connect_db(self):
    #     db_name = input("创建的数据库：")
    #     a = set_up.execute('create database if not exists {0}'.format(db_name))

    """查看表是否存在"""
    def insert_table(self):
        # create = self.cursor.execute('')
        self.table = input('查找数据表没有则创建:')
        select_table_sql =self.cursor.execute('show tables like "%s"'%self.table)
        if select_table_sql == 1:
            print("数据表存在")
        else:
            print("数据表不存在")
            create_table_sql =f'create table {self.table} (serial varchar(200), movies_name varchar(20) ,movies_data varchar(20))'
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            print("已创建")

    """插入数据"""
    def insert_data(self, value1):
        movie = self.table
        insert_data_sql = f"INSERT INTO {movie}(serial, movies_name, movies_data) values(%s, %s, %s)"
        self.cursor.execute(insert_data_sql, value1)
        self.conn.commit()

    """关闭游标，MySQL"""
    def close_mysql(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    con = Connect_mysql()


