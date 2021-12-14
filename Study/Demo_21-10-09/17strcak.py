'''
@Time    : 2021/10/12 15:04
@Author  : LKT
@FileName: 17strcak.py
@Software: PyCharm
 
'''
import requests
import json
import execjs

headers = {
    'cookie': 'Last-Event-ID=65736c61662f38392f38356666393765643936312f67736d2d616964656d2d756e656d2d6e776f64706f72642d71792065646968112246b0fd1004bdb6f4',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

with open('17track.js', 'r', encoding='utf-8') as f:
    track_js = f.read()
a = '657572742f3130332f32396337646432376337312f633362646266343734623a373930393934323838313a65736c61663a6e74622d756e656d2d656c69626f6d2d71792064657370616c6c6f632065736f6c632d7265677275626d6168207265677275626d616820656c67676f742d72616276616e1132f93853c310b1918'

data = '{"guid":"","data":[{"num":"9400128206335448109292"}],"timeZoneOffset":-480}'
print(a)
print(len(a))
ctx = execjs.compile(track_js)
event_id = ctx.call('get_cookie', data)
print(event_id)
print(len(event_id))
headers['cookie'] = 'Last-Event-ID=' + event_id
print(headers['cookie'])
response = requests.post('https://t.17track.net/restapi/track', headers=headers, data=data)
content = response.json()
print(content)
# print(json.dumps(content, indent=2, ensure_ascii=False))

