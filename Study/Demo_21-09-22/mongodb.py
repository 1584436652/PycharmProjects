import requests

from lxml import etree
from pymongo import MongoClient
from retry import retry


class WuHanWeather(object):

    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/92.0.4515.159 Safari/537.36"
        }
        # mongodb数据库操作对象
        self.client = MongoClient(host='127.0.0.1', port=27017)
        # 数据插⼊的数据库与集合
        self.coll = self.client["Weather"]["wuhan"]

    @retry(tries=3)
    def make_response(self, url):
        print(f'正在请求--{url}')
        response = requests.get(url=url, headers=self.headers)
        html_data = response.text
        assert response.status_code == 200
        return html_data

    def parse(self, res):
        html = etree.HTML(res)
        for i in range(2, 33):
            try:
                date = html.xpath(f'//div[@id="content"]//tr[{i}]//td[1]//a/text()')[0].strip()
                temperature = html.xpath(f'//div[@id="content"]//tr[{i}]//td[3]/text()')[0].split()
                max_temperature = temperature[0]
                min_temperature = temperature[2]
                item = dict()
                item["日期"] = date
                item["气温"] = [max_temperature, min_temperature]
                print(item)
                yield item
            except IndexError:
                break

    def insert_mongodb(self, item):
        for items in item:
            # 用update去重
            self.coll.update_many({"日期": items["日期"]}, {'$set':{"气温": items["气温"]}}, True)
            # self.coll.insert_one(items)

    def main(self):
        for j in range(2021, 2022):
            for join_url in range(1, 3):  # 13
                if join_url <= 9:
                    start_url = f'http://www.tianqihoubao.com/lishi/wuhan/month/{j}0{join_url}.html'
                    make = self.make_response(start_url)
                    html = self.parse(make)
                    mg = self.insert_mongodb(html)
                else:
                    start_url = f'http://www.tianqihoubao.com/lishi/wuhan/month/{j}{join_url}.html'
                    make = self.make_response(start_url)
                    html = self.parse(make)
                    mg = self.insert_mongodb(html)

    def __del__(self):
        print('关闭')
        self.client.close()


wuhan = WuHanWeather()
wuhan.main()