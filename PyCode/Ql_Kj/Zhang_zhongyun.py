# -*- coding:utf-8 -*-
import json
import time
import requests
import pandas as pd
import xlwt

headers = {
    'cookie':'_uab_collina=157103605824386357554084; last_read_notice_id_101628=427; last_read_notice_id_98156=427; aliyungf_tc=AQAAAIwUIjF/jgoA4h0Otx7ipstgP0+p; user_token=e0958bab535343c688b98e9e2ac5334e; last_read_notice_id_98157=435',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
html = requests.get('https://inovel.818tu.com/backend/order_stats/api_get_daily_stats/?limit=5000&last_date=',headers=headers)
res = html.json()
print(res)
def timestamp_to_str(timestamp=None, format='%Y-%m-%d'):
    if timestamp:
        time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
        result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
        return result
    else:
        return time.strptime(format)

jsonfile = []

for i in res:
    dicts = {
        "日期":timestamp_to_str(int(i.get('date'))),
        "充值金额": float(i.get('paid_amount'))/100.00,
        "新用户充值": i.get('new_member_paid_amount'),
        "老用户充值": float(i.get('paid_amount'))/100,
        "普通充值": float(i.get('welth_order_paid_amount'))/100,
        "普通充值支付订单数":int(i.get('paid_order_count')),
        "年费VIP会员": float(i.get('vip_order_paid_amount'))/100,
        "年费VIP会员支付订单数": int(i.get('vip_order_paid_count')),
        }
    jsonfile.append(dicts)

print(jsonfile)


def jsonToexcel():
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('data')
    ll = list(jsonfile[0].keys())
    for i in range(0, len(ll)):
        sheet1.write(0, i, ll[i])
    for j in range(0, len(jsonfile)):
        m = 0
        ls = list(jsonfile[j].values())
        for k in ls:
            sheet1.write(j + 1, m, k)
            m += 1
    workbook.save('data.xls')
jsonToexcel()
# print(json.dumps( res,ensure_ascii=False,indent=2))