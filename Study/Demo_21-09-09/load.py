'''
@Time    : 2021/9/24 13:48
@Author  : LKT
@FileName: load.py
@Software: PyCharm

'''
import requests
import time
import re
import json
from retry import retry
from lxml import etree


class JD_Spider(object):

    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.159 Safari/537.36'

        }
        self.detail_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.159 Safari/537.36',
            'cookie': '__jdu=1623381615868142016504; shshshfpa=212e9fd0-d021-7b6a-4782-fc61e84171ac-1623381617; shshshfpb=affY7ziVhpdKFT%2FMQ1jQ1jA%3D%3D; __jdv=76161171|baidu|-|organic|not set|1631694810179; areaId=19; ipLoc-djd=19-1607-47388-0; PCSYCityID=CN_440000_440300_440309; __jdc=122270672; shshshfp=34781323cd39edde7c5b506732a88aeb; user-key=13b37289-2fc0-44be-a61d-e233e3898b21; __jda=122270672.1623381615868142016504.1623381615.1632469394.1632479807.11; TrackID=1hWyI9klPPTgc3SVtc2mQfcH0N2oBIkrGmqjyckrdlZ1KbUeuXOiizS8E7QKbtQTIA1EGlQdBlx97J9vEfmfZ2J6k8poH8q2xRyLD9wYl6Ec; thor=3226C86F5E4024DE10E4641507D518D8F417E0FC3F882E8F8352ABC360D5CF508BDD4518F7E5F9B0B054685BCD7A8DCD07062DEDBC25D7CEDF1579EF482591AC16D2CF50003C132E389FCEE35E28F805C795EA7A9060D956221BA5FF3DDED40BC9205CC54312B879761B5D99BFFAA538C7B0AB62FD736380F492100893FFF205598DC730FFB29017309DE0715CAFB43C36B7707AF3B627B41FA895495340B675; pinId=_KBmia43MsAIfevcwkAvy7V9-x-f3wj7; pin=jd_408dda6b354f6; unick=jd_408dda6b354f6; ceshi3.com=000; _tp=MwBm3a5MnsKZtDI%2FcX4jtxvkT8iv9ObGTAEMdwBDwAU%3D; _pst=jd_408dda6b354f6; token=2b40971343648f090570658a02fb6c12,3,906933; __tk=uSq0upJxvU20YDiRYpr3v3hyZpqzY3iRvcr3YSkwvsX,3,906933; shshshsID=1e00c6494ad9e13d886552255619cada_2_1632479927525; __jdb=122270672.32.1623381615868142016504|11.1632479807; wlfstk_smdl=d33831qwhycqrwvf00j31hsvdsu2ym1c; 3AB9D23F7A4B3C9B=NJOESNKMW5YAAQ6XHQTFW6QKLH62WYSAMIN5QS2KZMRPHXN666RISRVWGQXQOJEE4GJXUST75KUHGL5JZQSICHZRDY',
            'referer': 'https://passport.jd.com/'
        }
        self.start_url = 'https://search.jd.com/Search?'
        self.first30_params = {
            'keyword': "电脑",
            'enc': 'utf-8'
        }
        # self.after30_url = 'https://search.jd.com/s_new.php?'
        # now_time = time.time()
        # conversion_time = '%.4f' % now_time
        # self.after30_params = {
        #     'keyword': "电脑",
        #     'pvid': '45304335784849adb9a5214a8d07e5f7',
        #     'page': 2,
        #     's': 27,
        #     'scrolling': conversion_time,
        #     'tpl': "1_M",
        #     'isList': 0
        # }

    @retry(tries=3)
    def make_response(self, url, headers, params=None):
        res = requests.get(url=url, headers=headers, params=params)
        jd_res = res.text
        assert res.status_code == 200
        return jd_res

    def parse_url(self, res):
        data_list = []
        https_url_join = "https:"
        res_html_data = etree.HTML(res)
        for i in range(1, 31):
            jd_shop_url = res_html_data.xpath(f'//*[@id="J_goodsList"]//ul//li[{i}]//div[3]//a/@href')[0]
            url_join = f'{https_url_join}{jd_shop_url}'
            data_list.append(url_join)
        after_id = re.findall(r"search000014_log:(.+?),uuid", res, re.S)
        split_id = re.findall(r"\d+", after_id[0], re.S)
        for j in split_id:
            after_shop_url = f'https://item.jd.com/{j}.html'
            data_list.append(after_shop_url)
        return data_list

    def detail_parse(self, url_res):
        detail_html = etree.HTML(url_res)
        title = detail_html.xpath('//div[@class="product-intro clearfix"]//div[@class="sku-name"]/text()') # 标题
        a = json.dumps(title, ensure_ascii=False)
        print(type(a))
        print(a.strip(' '))
        # price = detail_html.xpath('//div[@class="product-intro clearfix"]//div[@class="summary summary-first"]//div[@class="dd"]//span[@class="p-price"]//span')
        # for i in price:
        #     print(i.text)
        comments = detail_html.xpath('//div[@class="product-intro clearfix"]//div[@id="comment-count"]//a/text()')
        print(comments)


    def main(self):
        first30_res_html = self.make_response(self.start_url, self.headers, self.first30_params)
        first30_html = self.parse_url(first30_res_html)
        for detail_url in first30_html:
            print(detail_url)
            url_shop_detail = self.make_response(detail_url, self.detail_headers)
            self.detail_parse(url_shop_detail)


jd = JD_Spider()
jd.main()