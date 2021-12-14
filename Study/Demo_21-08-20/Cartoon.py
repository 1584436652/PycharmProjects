import requests
import time
import os
import re
from lxml import etree
from fake_useragent import UserAgent


class Cartoon_Wallpaper(object):

    def __init__(self):
        self.home_url = 'https://pic.netbian.com'
        self.url = 'https://pic.netbian.com/4kdongman/index_'
        self.location = os.getcwd() + '/fake_useragent.json'
        ua = UserAgent(path=self.location)
        self.headers = {
            # 'content-encoding': 'gzip',
            # 'content-length': '4020',
            # 'content-type': 'text/html',
            # 'date': 'Thu, 02 Sep 2021 10:06:02 GMT',
            # 'last-modified': 'Wed, 01 Sep 2021 15:32:21 GMT',
            # 'server': 'yunjiasu',
            # 'strict-transport-security': 'max-age=31536000',
            # 'vary': 'Accept-Encoding',
            # 'yjs-id': 'a73cad67806c32d1-130',
            # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'accept-encoding': 'gzip, deflate, br',
            # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            # 'cache-control': 'max-age=0',
            # 'cookie': '__yjs_duid=1_024160bd6ffd7efac888bfe75a6fa32d1630487055658; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1630487578,1630487610; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1630487596,1630487612,1630487624,1630555246; zkhanlastsearchtime=1630567501; zkhanecookieclassrecord=%2C66%2C59%2C55%2C68%2C65%2C63%2C62%2C53%2C54%2C60%2C58%2C67%2C; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1630577159',
            # # 'if-modified-since': 'Wed, 01 Sep 2021 15:32:21 GMT',
            # 'referer': 'https://pic.netbian.com/4kdongman/index_2',
            # 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-fetch-dest': 'document',
            # 'sec-fetch-mode': 'navigate',
            # 'sec-fetch-site': 'same-origin',
            # 'sec-fetch-user': '?1',
            # 'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',

            # 'user-agent': ua.random,
        }
        # self.pr = {
        #     'https':'117.187.167.224:3128'
        # }
        print(self.headers)

    def get_img_src(self, page):
        self.url_data = []
        self.name_data = []
        url = f'{self.url}{page}.html'
        print(url)
        res = requests.get(url=url, headers=self.headers)
        print(f'响应为：{res.status_code}')
        res.encoding = 'gbk'
        res_html = res.text
        # print(res_html)
        data = etree.HTML(res_html)
        url_a_img = data.xpath('//div[@id = "main"]//ul[@class="clearfix"]//a[@target="_blank"]/img/@src')
        b_text = data.xpath('//div[@id = "main"]//ul[@class="clearfix"]//a[@target="_blank"]/b/text()')
        try:
            next_page = data.xpath('//*[@id="main"]//a[text()="下一页"]/text()')
            # print(next_page)
            for i, j in zip(url_a_img, b_text):
                add_img_url = '{0}{1}'.format(self.home_url, i)
                self.url_data.append(add_img_url)
                self.name_data.append(j)
            return next_page[0]
            # print(self.url_data)
        except Exception:
            return None

    def save_to_img(self):
        current_path = os.getcwd()
        file = f'{current_path}\{self.file_path}'
        if not os.path.exists(file):
            os.mkdir(file)
        for url, name in zip(self.url_data, self.name_data):
            name_clear = re.sub(r'\W', ' ', name)
            img = '{0}/{1}.jpg'.format(file, str(name_clear))
            with open(img, 'wb') as fp:
                res = requests.get(url=url,  headers=self.headers)
                print(f'{name}-----正在下载中...')
                # print(res.status_code)
                data = res.content
                fp.write(data)
                time.sleep(1)

    def main(self):
        self.file_path = input('输入存入的文件夹：')
        page = 2
        while True:
            next_page = cartoon.get_img_src(page)
            if next_page == "下一页":
                cartoon.save_to_img()
                print('\n')
            elif next_page == None:
                cartoon.save_to_img()
                print('\n')
                print('----我也是有底线的！！！----')
                break
            page += 1


cartoon = Cartoon_Wallpaper()
cartoon.main()
