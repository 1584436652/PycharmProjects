from pymongo import MongoClient
from config import *

def mongodb2csv():
    # mongodb数据库操作对象
    client = MongoClient(Mongodb_URL)
    # 数据插⼊的数据库与集合
    coll = client[Mongodb_DB][Mongodb_TABLE]
    # 条件
    my_query = {'日期': "2008年01月01日"}
    # 要改的
    demo = {"$set": {'气温': ['190','200']}}
    coll.update_many(my_query, demo, True)

mongodb2csv()

