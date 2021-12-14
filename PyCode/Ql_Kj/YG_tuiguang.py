from __future__ import division
import time
import requests
import xlwt
import uuid
# 抓取阳光书城的推广列表数据


headers = {
    'Referer': 'https://admin.yifengaf.cn/admin/referral/referral?addtabs=1&push=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Cookie': 'PHPSESSID=udsnbanb0qad90fvf96cb0hu9q; SERVERID=7eb230e9bc238fb3873ddb90b8448727|1574402341|1574402182',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest'
}

html = requests.get('https://admin.yifengaf.cn/admin/referral.referral/index?push=0&sort=state+desc%2Cid+desc&order=&offset=0&limit=1000&filter=%7B%7D&op=%7B%7D&_=1574402341125',headers=headers)
res = html.json()
jsonfile = []
# def timestamp_to_str(timestamp=None, format='%Y-%m-%d'):
#     if timestamp:
#         time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
#         result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
#         return result
#     else:
#         return time.strptime(format)

for i in res['rows']:
    dicts = {
        "派单渠道":i.get('name'),
        "总阅读数": i.get('uv'),
        "总关注人数": i.get('follow'),
        "总充值金额": float(i.get('money')),

        }
    jsonfile.append(dicts)
print(jsonfile)
#
def jsonToexcel():
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('data')
    ll = list(jsonfile[0].keys())
    rd = uuid.uuid4()
    for i in range(0, len(ll)):
        sheet1.write(0, i, ll[i])
    for j in range(0, len(jsonfile)):
        m = 0
        ls = list(jsonfile[j].values())
        for k in ls:
            sheet1.write(j + 1, m, k)
            m += 1
    workbook.save('祺量%s.xls' % rd)


jsonToexcel()



