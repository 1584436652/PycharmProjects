import requests
import json


class Track_17(object):

    def __init__(self, cookie=None):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/92.0.4515.159 Safari/537.36",
            'Referer': 'https://t.17track.net/zh-cn',
            'Cookie': cookie
        }
        self.proxies = {
            # "https": "https://113.96.219.105:4015"
        }
        self.url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=zh-Hans'
        self.data = [
            [{"text": "Csomaglogisztikai Központ, Returned to sender"},
             {"text": "Szentendre 1 posta, Forwarding for delivery"},
             {"text": "Szentendre 1 posta, Cannot be delivered (refused acceptance)"},
             {"text": "Szentendre 1 posta, Processing on arrival at premises"},
             {"text": "Bp. 6. sz. Csomagkézbesítő Bázis, Forwarding for delivery"},
             {"text": "Unsuccessful delivery attempt"},
             {"text": "Bp. 6. sz. Csomagkézbesítő Bázis, Closure of allocation data"},
             {"text": "Bp. 6. sz. Csomagkézbesítő Bázis, Arrival for processing"},
             {"text": "Csomaglogisztikai Központ, Forwarding for delivery"},
             {"text": "Csomaglogisztikai Központ, Acceptance completed"},
             {"text": "0, Notification received, we start the process when getting item from the sender"}]
        ]

    def make_response(self, url):
        print(f'正在请求--{url}')
        response = requests.post(url=url, headers=self.headers, data=json.dumps(self.data), proxies=self.proxies)
        print(response.status_code)
        html_data = response.text
        print(html_data)


with open('cookie.txt', 'r', encoding='utf-8') as fp:
    cookie = fp.read()
track = Track_17(cookie)
print(track.url)
track.make_response(track.url)