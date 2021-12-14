import time

import requests
from retrying import retry


class BaseSpider(object):
    """爬虫基类"""

    def __init__(self):
        self.start_urls = ["https://www.baidu.com"]
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        'Cookie': 'v_21924_setting_grading_menu_open=%5Bnull%2Cnull%5D; v_21924_setting_grading_menu_off=%5B0%2C1%2C2%5D; ucode=4783ab83b2acfbb81dddf86745a73144; v_21890_setting_grading_menu_open=%5B%5D; v_21890_setting_grading_menu_off=%5B0%5D'
    }
    @retry(stop_max_attempt_number=2)
    def __parse_url(self,url):
        """爬"""
        print(f"开始请求: [{url}]")
        resp = requests.get(url, headers = self.headers,timeout=3)
        assert  resp.status_code == 200

        return resp.content.decode()

    def parse_url(self,url):
        """转发"""
        try:
            resp = self.__parse_url(url)
            # time.sleep(1.2)
        except AssertionError as why:
            resp =None
        return resp

    def get_data(self, resp):
        """取"""
        raise NotImplementedError

    def save_data(self,data):
        """存"""
        raise  NotImplementedError

    def export_excel(self,export):
        """excel"""
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