import json
def config():
    with open('config.json', 'r') as fp:
        dicts = fp.read().encode(encoding='gbk').decode(encoding='utf-8')
        message = json.loads(dicts, encoding='GBK',)
        print(message)

config()