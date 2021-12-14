import execjs
import time
import hashlib
import base64
import requests
import xlwt


def time_stamp():
    times = time.time()
    # rd = (int(round(times*1000)))
    # str_text = str(round(rd/1000))
    str_text = str(round(times))
    # print(str_text)
    # str_text1 ='1629263208'
    return str_text


def get_str_sha1_secret_str(res:str):
    url_text = '/api/movie,'
    make_up_first = url_text + res
    # print(make_up_first)
    sha = hashlib.sha1(make_up_first.encode('utf-8'))
    encrypts = sha.hexdigest()
    # print(encrypts)
    return encrypts


def base64_str(sha1_str):
    make_up_second =sha1_str + ',' + time_stamp()
    bytes_url = make_up_second.encode("utf-8")
    str_url = base64.b64encode(bytes_url)
    str_url_text = str((str_url))
    token = str_url_text[2:-1]
    # print(text)
    return token


def get_html(token, page):
    offset = 0
    data_list = []
    for i in range(1, page+1):
        url = 'https://spa2.scrape.center/api/movie/?'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0'
                          '.4472.164 Safari/537.36'
        }
        data = {
            'limit': 10,
            'offset': offset,
            'token': token
        }
        res = requests.get(url=url, headers=headers, params=data)
        offset += 10
        json_data = res.json()
        print(type(json_data))
        for i in json_data["results"]:
            dicts = {
                "id": i.get("id"),
                "name": i.get("name"),
                "published_at": i.get("published_at")
            }
            print(dicts)
            data_list.append(dicts)
    return data_list


def save_xls(data_list):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('movie', cell_overwrite_ok=True)
    title = list(data_list[0].keys())
    # print(len(data_list))
    for titles in range(0, len(title)):
        sheet.write(0, titles, title[titles])
    for i in range(0,len(data_list)):
        values_str = list(data_list[i].values())
        # print(values_str)
        count = 0
        for j in values_str:
            sheet.write(i+1, count, j)
            # print(count)
            count += 1
            # print(j)
    workbook.save('movie.xls')


page = int(input('爬取的总页数：'))
token = base64_str(get_str_sha1_secret_str(time_stamp()))
save_xls(get_html(token, page))

