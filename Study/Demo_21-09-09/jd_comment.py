'''
@Time    : 2021/9/25 10:57
@Author  : LKT
@FileName: jd_comment.py
@Software: PyCharm
 
'''
import jieba
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud

import requests
import time
import re
import json
from pymongo import MongoClient
from retry import retry


class JD_Comment_Spider(object):

    def __init__(self):
        self.detail_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.159 Safari/537.36',
            # 'cookie': '__jdu=1623381615868142016504; shshshfpa=212e9fd0-d021-7b6a-4782-fc61e84171ac-1623381617; shshshfpb=affY7ziVhpdKFT%2FMQ1jQ1jA%3D%3D; __jdv=76161171|baidu|-|organic|not set|1631694810179; areaId=19; ipLoc-djd=19-1607-47388-0; PCSYCityID=CN_440000_440300_440309; __jdc=122270672; shshshfp=34781323cd39edde7c5b506732a88aeb; user-key=13b37289-2fc0-44be-a61d-e233e3898b21; __jda=122270672.1623381615868142016504.1623381615.1632469394.1632479807.11; TrackID=1hWyI9klPPTgc3SVtc2mQfcH0N2oBIkrGmqjyckrdlZ1KbUeuXOiizS8E7QKbtQTIA1EGlQdBlx97J9vEfmfZ2J6k8poH8q2xRyLD9wYl6Ec; thor=3226C86F5E4024DE10E4641507D518D8F417E0FC3F882E8F8352ABC360D5CF508BDD4518F7E5F9B0B054685BCD7A8DCD07062DEDBC25D7CEDF1579EF482591AC16D2CF50003C132E389FCEE35E28F805C795EA7A9060D956221BA5FF3DDED40BC9205CC54312B879761B5D99BFFAA538C7B0AB62FD736380F492100893FFF205598DC730FFB29017309DE0715CAFB43C36B7707AF3B627B41FA895495340B675; pinId=_KBmia43MsAIfevcwkAvy7V9-x-f3wj7; pin=jd_408dda6b354f6; unick=jd_408dda6b354f6; ceshi3.com=000; _tp=MwBm3a5MnsKZtDI%2FcX4jtxvkT8iv9ObGTAEMdwBDwAU%3D; _pst=jd_408dda6b354f6; token=2b40971343648f090570658a02fb6c12,3,906933; __tk=uSq0upJxvU20YDiRYpr3v3hyZpqzY3iRvcr3YSkwvsX,3,906933; shshshsID=1e00c6494ad9e13d886552255619cada_2_1632479927525; __jdb=122270672.32.1623381615868142016504|11.1632479807; wlfstk_smdl=d33831qwhycqrwvf00j31hsvdsu2ym1c; 3AB9D23F7A4B3C9B=NJOESNKMW5YAAQ6XHQTFW6QKLH62WYSAMIN5QS2KZMRPHXN666RISRVWGQXQOJEE4GJXUST75KUHGL5JZQSICHZRDY',
        }
        self.detail_url = 'https://club.jd.com/comment/skuProductPageComments.action?'
        # mongodb数据库操作对象
        self.client = MongoClient(host='127.0.0.1', port=27017)
        # 数据插⼊的数据库与集合
        self.coll = self.client["JD"]["comment"]

    @retry(tries=3)
    def make_response(self, url, headers, params=None):
        res = requests.get(url=url, headers=headers, params=params)
        jd_res = res.text
        assert res.status_code == 200
        return jd_res

    def comment_parse(self, shop_comment):
        sub_res_json = re.sub(u"\\(.*?", '', shop_comment)
        end_res = sub_res_json.replace(sub_res_json[-2], "")
        end_replace = end_res.strip(';')
        split_jd_res = end_replace.lstrip('fetchJSON_comment98')
        jd_res_json = json.loads(split_jd_res)
        comments = jd_res_json['comments']
        lists = []
        for items in comments:
            dicts = {
                "nickname": items.get('nickname'),
                'content': items.get('content'),
                'creation_time': items.get('creationTime'),
            }
            lists.append(dicts)
        return lists

    def save_to_mongodb(self, item):
        for result in item:
            self.coll.update_many({"nickname": result["nickname"]},
                                  {'$set':{"content": result["content"],
                                           "creation_time": result["creation_time"]}} , True)
            # print(result["content"])

    def save_to_txt(self, str_txt):
        for i in str_txt:
            self.txt_text.append(i["content"])

    def would_cloud(self, data):
        jieba.setLogLevel(jieba.logging.INFO)
        # 使用 jieba 进行分词
        cut = jieba.cut(data)
        string = ' '.join(cut)
        print(string)

        # 读取背景图片
        wc = WordCloud(font_path=r'C:\Windows\Fonts\simkai.ttf',  # 使用系统中的字体，注意中文展示
                       background_color='white',
                       width=1000,
                       height=800,
                       )
        # 根据文本生成词云
        wc.generate_from_text(string)
        process_word = WordCloud.process_text(wc, string)
        print(process_word)
        # 保存词云图片
        wc.to_file('test.png')  # 保存图片
        plt.imshow(wc)  # 用plt显示图片
        plt.axis('off')  # 不显示坐标轴
        plt.show()

    def main(self):
        self.txt_text = []
        input_url = input("商品链接：")
        product_id = re.findall(r'\d+', input_url)
        page = 0
        while True:
            detail_params = {
                'callback': 'fetchJSON_comment98',
                'productId': product_id[0],
                'score': 0,
                'sortType': 5,
                'page': page,
                'pageSize': 10,
                'isShadowSku': 0,
                'rid': 0,
                'fold': 1,
            }
            page += 1
            detail_html = self.make_response(self.detail_url, self.detail_headers, detail_params)
            detail_comment = self.comment_parse(detail_html)
            if detail_comment:
                print(f'页评论条数：{len(detail_comment)}')
                self.save_to_mongodb(detail_comment)
                self.save_to_txt(detail_comment)
                print('已完成第{}页存储'.format(page) + '\n')
            else:
                print("没有更多评论了...")
                break
        would_str = json.dumps(self.txt_text, ensure_ascii=False)
        self.would_cloud(would_str)



jd = JD_Comment_Spider()
jd.main()

