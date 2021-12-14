import requests
import json


def parameter(par: list, *args):
    """
    构造请求参数，参数需要一个列表传递，且列表长度为40
    :param par: 列表
    :param args: 传进两个参数， 列表开始和结尾的下标
    :return: 返回请求参数
    """
    messages = []
    for order in par[args[0]:args[1]]:
        result = {"num": order, "fc": 0, "sc": 0}
        messages.append(result)
    data = {
        "data": messages,
        "guid": "",
        "timeZoneOffset": -480
    }
    return data


url = 'https://t.17track.net/restapi/track'

headers = {
    'Content-Type': 'application/json',
    'Referer': 'https://t.17track.net/zh-cn',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    'cookie': "_yq_bid=G-039EA606EE3FC937; _ga=GA1.2.986231122.1627977926; v5_AppIconsVersion=1; _ati=6751970764804; __gads=ID=e5782eb6fbd91ffc:T=1627981180:S=ALNI_MaAkov2SVdmkxxoQgBBG85dYlotUg; v5_Culture=zh-cn; country=CN; v5_HisExpress=190208_01151_100018; v5_TranslateLang=zh-Hans; _gid=GA1.2.1377430753.1637891982; _gat_cnGa=1; Last-Event-ID=657572742f6664312f35326238386639356437312f663963643933326565333a373930393934323838313a65736c61663a7261626c6f6f742d72616276616e2d7179206c6c75662d73692076616e2d72616276616e2076616e16236f41805e4078eb71"
          }
proxies = {'http': 'https://124.204.33.162:8000'}
da = parameter(['523000012168200009342258'], 0, 40)
print(da)
response = requests.post(url=url, headers=headers, data=json.dumps(da), proxies=proxies)
print(response.status_code)
html_data = response.json()
print(html_data)
