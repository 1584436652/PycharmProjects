import requests
import time
import hashlib
import base64
import requests
import xlwt
import threading
from mysql_data import Connect_mysql
from retry import retry


class Demo(object):

    def __init__(self):
        # self.url = 'https://spa2.scrape.center/api/movie/?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0'
                          '.4472.164 Safari/537.36'
        }
        self.url_text = '/api/movie,'

    @retry(tries=1)
    def parse_url(self, url):
        # print(f"开始请求: [{url}]")
        resp = requests.get(url, headers=self.headers)
        assert resp.status_code == 200
        # print(type(resp.json()))
        # print(resp.json())
        res = resp.json()
        return res

    def resp_data_judge(self,url):
        try:
            resp = self.parse_url(url)
        except Exception as why:
            resp =None
            # print(resp)
        return resp

    def time_stamp(self):
        times = time.time()
        str_text = str(round(times))
        return str_text

    def get_str_sha1_secret_str(self):
        url_text = self.url_text
        make_up_first = url_text + self.time_stamp()
        sha = hashlib.sha1(make_up_first.encode('utf-8'))
        encrypts = sha.hexdigest()
        return encrypts

    def base64_str(self):
        make_up_second = self.get_str_sha1_secret_str() + ',' + self.time_stamp()
        bytes_url = make_up_second.encode("utf-8")
        str_url = base64.b64encode(bytes_url)
        str_url_text = str((str_url))
        token = str_url_text[2:-1]
        # print(token)
        return token

    def get_html(self, page):
        offset = 0
        data_list = []
        for pages in range(1, page+1):
            url = f'https://spa2.scrape.center/api/movie/?limit=10&offset={offset}&token={self.base64_str()}'
            offset += 10
            data_json = self.resp_data_judge(url)
            if data_json != None:
                if len(data_json["results"]) != 0:
                    for i in data_json["results"]:
                        dicts = {
                            "id": i.get("id"),
                            "name": i.get("name"),
                            "published_at": i.get("published_at")
                        }
                        # print(dicts)
                        data_list.append(dicts)
                    print(f"爬取第{pages}页成功")
                else:
                    print(f"请求第{pages}页成功，但没有数据")
            else:
                # print(data_json)
                print(f"请求两次之后失败，爬取第{pages}页失败")
        # print(data_list)
        return data_list

    def save_mysql(self):
        print("处理mysql-ing")
        for i in self.get_html(page):
            mysql_data = list(i.values())
            con1.insert_data(mysql_data)

    def save_xls(self):
        print("处理excel-ing")
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('movie', cell_overwrite_ok=True)
        data_list = self.get_html(page)
        title = list(data_list[0].keys())
        # print(len(data_list))
        for titles in range(0, len(title)):
            sheet.write(0, titles, title[titles])
        for i in range(0, len(data_list)):
            values_str = list(data_list[i].values())
            # print(values_str)
            count = 0
            for j in values_str:
                sheet.write(i + 1, count, j)
                # print(count)
                count += 1
                # print(j)
        workbook.save('movie.xls')


con1 = Connect_mysql()
con1.get_connect()
con1.insert_table()
demo = Demo()
page = int(input('爬取的总页数：'))
print("\n")
# t1 = threading.Thread(target=demo.save_xls())
# t2 = threading.Thread(target=demo.save_mysql())
# t1.start()
# t2.start()
# t1.join()
# t2.join()
demo.save_xls()
demo.save_mysql()
con1.close_mysql()

