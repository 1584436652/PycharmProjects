from bs4 import BeautifulSoup
from retry import retry
from multiprocessing.dummy import Pool
import time
import requests
from lxml import etree
import telnetlib
# html = """
# <html lang="en">
#     <head>
#       <meta charset="utf-8">
#       <meta name="theme-color" content="#ffffff">
#       <base href="./"><link rel="stylesheet" href="styles.30d0912c1ece284d8d9a.css">
#     </head>
#     <body>
#         <div>
#             <p>百里守约</p>
#         </div>
#         <div class="song">
#             <p>前程似锦</p>
#         </div>
#         <div class="song">
#             <p>前程似锦2</p>
#         </div>
#         <div class="ming">  #后面改了名字
#             <p>以梦为马</p>
#         </div>
#         <div class="tang">
#             <ul>
#                 <li><a href='http://123.com' title='qing'>清明时节</a></li>
#                 <li><a href='http://ws.com' title='qing'>秦时明月</a></li>
#                 <li><a href='http://xzc.com' title='qing'>汉时关</a></li>
#             </ul>
#         </div>
#       <flink-root></flink-root>
#         <script type="text/javascript" src="runtime.0dcf16aad31edd73d8e8.js"></script><script type="text/javascript" src="es2015-polyfills.923637a8e6d276e6f6df.js" nomodule></script><script type="text/javascript" src="polyfills.bb2456cce5322b484b77.js"></script><script type="text/javascript" src="main.8128365baee3dc30e607.js"></script>
#     </body>
# </html>
# """
# soup = BeautifulSoup(html, 'html.parser')
# print(type(soup.meta))
# # print(soup.div)
# # print(soup.find('div'))
# # print(soup.find('div', class_="ming"))
# a = soup.findAll('p')[0]
# print(type(a))
# print(soup.select('.tang'))
# print('*'*50)
# print(soup.select('.tang > ul > li > a')[1])
# print(soup.select('.tang   a')[0].text)

class Demo(object):

    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/92.0.4515.159 Safari/537.36"
        }
        self.url89 = 'https://www.89ip.cn/index_{}.html'
        self.proxies = {
            'https': 'https://182.84.144.54:3256',
    }

    @retry(tries=3)
    def make_response(self, url):
        print(f'正在请求--{url}')
        try:
            response = requests.get(url=url, headers=self.headers, proxies = self.proxies)
            html_data = response.text
            print(html_data)
            assert response.status_code == 200
            return html_data
        except Exception as e:
            print(e)
            return None

    def parse89(self, res):
        # soup = BeautifulSoup(res, 'html.parser')
        # result = soup.find('table', class_="layui-table")
        # print(result)
        # a = soup.findAll('td')
        # c = 0
        # for i in range(1, 21):
        #     b = a[c].text
        #     c+=5
        #     print(b)
        dicts = {}
        html = etree.HTML(res)
        result = html.xpath('//table[@class="layui-table"]//tbody//tr')
        for i in result:
            ip = i.xpath('./td[1]/text()')[0].strip()
            post = i.xpath('./td[2]/text()')[0].strip()
            dicts[ip] = post
        return dicts

    def run(self):
        for page in range(1, 10):
            url = self.url89.format(page)
            res = self.make_response(url)
            data_dicts = self.parse89(res)
            for ip, post in data_dicts.items():
                print('{0}:{1}'.format(ip, post))
                self.test_ip(ip, post)


    def main(self):
        start = time.time()
        page_start = 0
        for i in range(0, 6):
            url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={page_start}'
            # lists.append(url)
            page_start += 20
            html = self.make_response(url)
            print(html)
            time.sleep(1.5)
        end = time.time()
        print(end - start)
        # print(lists)

    def main2(self):
        start = time.time()
        lists = []
        page_start = 0
        for i in range(0, 6):
            url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={page_start}'
            # lists.append(url)
            page_start += 20
            lists.append(url)
        pool = Pool(4)
        pool.map(self.make_response, lists)
        end = time.time()
        print(end - start)

    def test_ip(self, ip, port):
        try:
            telnetlib.Telnet(ip, port, timeout=2)
            print("代理ip有效！" + '\n')
        except:
            print("代理ip无效！" + '\n')


de = Demo()
de.main()
# de.test_ip('223.244.179.204', '3256')
# de.run()


# import base64
# import json
# import requests
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别 参考 https://shimo.im/docs/RPGcTpxdVgkkdQdY
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别
# def base64_api(uname, pwd, img, typeid):
#     with open(img, 'rb') as f:
#         base64_data = base64.b64encode(f.read())
#         b64 = base64_data.decode()
#     data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
#     result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
#     print(result)
#     if result['success']:
#         return result["data"]["result"]
#     else:
#         return result["message"]
#
#
# if __name__ == "__main__":
#     img_path = "C:/Users/Administrator/Desktop/a.png"
#     result = base64_api(uname='1584436652', pwd='lkt02230330', img=img_path, typeid=1)
#     print(result)

# img_path = "C:/Users/Administrator/Desktop/a.png"
#
# with open(img_path, 'rb') as f:
#     # print(f.read())
#     print('\n')
#     base64_data = base64.b64encode(f.read())
#     print(base64_data)
#     print('\n')
#     b64 = base64_data.decode()
#     print(b64)