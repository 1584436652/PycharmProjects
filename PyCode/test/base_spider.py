import time

import requests
from retrying import retry

class BaseSpider(object):
    """爬虫基类"""

    def __init__(self):
        self.start_urls = ["https://www.baidu.com"]
        self.headers ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
    @retry(stop_max_attempt_number=2)
    def __parse_url(self,url):
        """爬"""
        proxies = {
            "http": 'http://14.115.105.101:808',
            "http": 'http://115.171.85.66:9000',
            "http": 'http://125.46.0.62:53281',
        }
        print(f"开始请求: [{url}]")
        resp = requests.get(url, headers = self.headers,timeout=3,proxies=proxies)
        assert  resp.status_code == 200

        return resp.content.decode()

    def parse_url(self,url):
        """转发"""
        try:

            resp = self.__parse_url(url)
            time.sleep(1.2)
        except AssertionError as why:
            resp =None
        return resp

    def get_data(self, resp):
        """取"""
        raise NotImplementedError

    def save_data(self,data):
        """存"""
        raise  NotImplementedError
    
    def run(self,**kwargs):
        """启动爬虫"""
        for url in self.start_urls:
            resp = self.parse_url(url)
            # data = self.get_data(resp)
            for data in self.get_data(resp):
                if  kwargs.get("debug"):
                    #进入debug模式,不存
                    return
                self.save_data(data)