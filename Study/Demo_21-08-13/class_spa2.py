import execjs
import time
import hashlib
import base64
import requests
import xlwt


class Movie(object):

    def __init__(self):
        self.url = 'https://spa2.scrape.center/api/movie/?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0'
                          '.4472.164 Safari/537.36'
        }
        self.url_text = '/api/movie,'

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

    # @retry(stop_max_attempt_number=2)
    # def parse_url(self, url):
    #     """爬"""
    #     print(f"开始请求: [{url}]")
    #     resp = requests.get(url, headers=self.headers, timeout=3)
    #     assert resp.status_code == 200
    #     print()
    #     return resp.content.decode()


    def get_html(self, page):
        offset = 0
        data_list = []
        for pages in range(1, page + 1):
            data = {
                'limit': 10,
                'offset': offset,
                'token': self.base64_str()
            }
            res = requests.get(url=self.url, headers=self.headers, params=data)
            if res.status_code ==200:
                offset += 10
                json_data = res.json()
                # print(type(json_data))
                for i in json_data["results"]:
                    dicts = {
                        "id": i.get("id"),
                        "name": i.get("name"),
                        "published_at": i.get("published_at")
                    }
                    print(dicts)
                    data_list.append(dicts)
                print(f"爬取第{pages}页成功")
            else:
                break
        return data_list

    def save_xls(self, data_list):
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('movie', cell_overwrite_ok=True)
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


page = int(input('爬取的总页数：'))
movie = Movie()
movie_data_list = movie.get_html(page)
movie.save_xls(movie_data_list)