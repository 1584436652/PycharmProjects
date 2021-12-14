'''
@Time    : 2021/9/28 10:36
@Author  : LKT
@FileName: my_session.py
@Software: PyCharm
 
'''
import requests
import json
import re
import math
from lxml import etree


class Demo_session(object):

    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.159 Safari/537.36'
        }
        # 首页
        self.home_page_url = 'https://900539.private.mabangerp.com/index.htm'
        # 登录接口
        self.login_url = 'https://900539.private.mabangerp.com/index.php?mod=main.doLogin'
        # 导航栏商品
        self.shop_url = 'https://900539.private.mabangerp.com/index.php?mod=stock.list&searchStatus=3'
        # 库存查询接口
        self.stock_url = 'https://private-amz.mabangerp.com/index.php?mod=warehouse.searchwarehousestock'
        # 存放库存
        self.results_dicts = {}

    def get_response(self, url, headers):
        return self.session.get(url=url, headers=headers)

    def post_response(self, url, headers, data=None):
        return self.session.post(url=url, headers=headers, data=data)

    # 登录参数
    def login_data(self, username, password):
        self.data = {
            "isMallRpcFinds": "",
            "username": username,
            "password": password,
        }

    # 库存参数
    def stock_data(self, page=1):
        with open('cMKey.txt', 'r', encoding='utf-8') as fp:
            cMKey = fp.read()
        self.stock_datas = {
            'stockOrderby': '',
            'search-content': 'stocksku',
            'stockQuantitytype': 'stockQuantitygt',
            'stockWarningQuantitytype': 'stockWarningQuantitygt',
            'parentCategoryId': '',
            'categoryId': '',
            'QuickSearchConditionId': '',
            'search-content-text1': '',
            'page': page,   # 每页的条数
            'rowsPerPage': 500,   # 修改这个参数时， stock_total()函数也要改
            'warehouseId': 1014254,   # 仓库参数，当前为广州仓
            'stockQuantitynum': 0,    # 查询的库存参数大于多少
            'stockWarningQuantitynum': '',
            'cMKey': cMKey,
            'lang': 'cn'
        }

    # 获取cMKey
    def shop_page(self):
        res = self.get_response(self.shop_url, self.headers)
        shop_res = res.text
        keys = re.findall(r"cMKey=(.+?)&lang", shop_res, re.S)[0]
        with open('cMKey.txt', 'w', encoding='utf-8') as fp:
            fp.write(keys)
        print("cMKey:{}".format(keys))
        # return keys

    # 获取总库存条数
    def stock_total(self):
        res = self.post_response(self.stock_url, self.headers, self.stock_datas)
        json_data = res.json()["pageHtml"]
        total = re.findall(r"class=\"semibold\">(.+?)</span>条", json_data, re.S)[0]
        divide = int(total) / 500
        totals = math.ceil(divide)
        return totals

    # 库存存入
    def stock_search(self):
        res = self.post_response(self.stock_url, self.headers, self.stock_datas)
        json_data = res.json()["message"]
        data = etree.HTML(json_data)
        pages = 1
        while True:
            try:
                sku = data.xpath(f'//li[{pages}]/ul/li[2]/p[1]/a/text()')[0]
                stock = data.xpath(f'//li[{pages}]/ul/li[6]/text()')[0]
                self.results_dicts[sku] = int(stock)
                # print(sku, stock)
                pages += 1
            except IndexError:
                break

    def main(self):
        self.session = requests.session()
        try:
            print("获取库存中")
            self.stock_data()
            stock_page = self.stock_total()
            for number in range(1, int(stock_page+1)):
                self.stock_data(number)
                self.stock_search()
        except json.decoder.JSONDecodeError:
            print("cMKey过期了，重新登录获取")
            # 先请求首页
            self.get_response(self.home_page_url, self.headers)
            self.login_data("13677395742", "d6qE37SZ")
            login_res = self.post_response(self.login_url, self.headers, self.data)
            # 判断登录后返回的键success的值是否为True
            if login_res.json()["success"]:
                print("登录成功")
                self.shop_page()
                self.stock_data()
                stock_page = self.stock_total()
                for number in range(1, int(stock_page + 1)):
                    self.stock_data(number)
                    self.stock_search()
        # print(self.results_dicts)
        # print(len(self.results_dicts))
        return self.results_dicts


if __name__ == '__main__':
    Demo_session().main()




