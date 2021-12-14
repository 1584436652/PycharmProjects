from __future__ import division
import time
import requests
import xlwt
import uuid



headers = {
    'Referer': 'https://vip.yifengaf.cn/admin/vip/admin/ordercollect/index?addtabs=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Cookie': 'PHPSESSID=cb4ep1t0mcg44rga113ggjcg7a; keeplogin=13072%7C604800%7C1573546728%7C5fd47f25c1b364bb9601a39f391b6136',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest'
}

html = requests.get('https://vip.yifengaf.cn/admin/vip/admin/ordercollect/index?tab=month&sort=createdate&order=desc&offset=0&limit=200&filter=%7B%22create_month%22%3A%222019-09%22%7D&op=%7B%22create_month%22%3A%22%3D%22%7D&_=1572943112504',headers=headers)
res = html.json()
jsonfile = []
# def timestamp_to_str(timestamp=None, format='%Y-%m-%d'):
#     if timestamp:
#         time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
#         result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
#         return result
#     else:
#         return time.strptime(format)

# def timestamp_to_str(timestamp=None, format='%Y-%m-%d'):
#     if timestamp:
#         time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
#         result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
#         return result
#     else:
#         return time.strptime(format)
for i in res['rows']:
    dicts = {
        "日期":i.get('create_month'),
        "公众号": i.get('wx_nickname'),
        "总充值": float(i.get('recharge_money')),
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



