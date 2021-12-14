# -*- coding:utf-8 -*-
import json
import time
import requests
import pandas as pd
import xlwt

headers = {
    'cookie':'aliyungf_tc=AQAAAK87SHd+xwIAM65XcRFLtE0uMWlC; _uab_collina=157215470448334512750958; user_token=fd36856a102e41718ab0b85635a009f2; last_read_notice_id_98157=433',
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
    # data = []  # 用于存储每一行的Json数据
    #
    # data.append(dicts)
    #
    # df = pd.DataFrame()  # 最后转换得到的结果
    # for line in data:
    #
    #     df1 = pd.DataFrame(line)
    #     df = df.append(df1)
    #
    #
    # # 在excel表格的第1列写入, 不写入index
    # df.to_excel('data.xlsx', sheet_name='Data', startcol=0, index=False)



# def jsonToexcel():
#
#     workbook = xlwt.Workbook()
#     sheet1 = workbook.add_sheet('data')
#     ll = list(jsonfile[0].keys())
#     for i in range(0, len(ll)):
#         sheet1.write(0, i, ll[i])
#     for j in range(0, len(jsonfile)):
#         m = 0
#         ls = list(jsonfile[j].values())
#         for k in ls:
#             sheet1.write(j + 1, m, k)
#             m += 1
#     workbook.save('data.xls')
#
#
# jsonToexcel()

# print(json.dumps( res,ensure_ascii=False,indent=2))