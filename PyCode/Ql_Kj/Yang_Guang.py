from __future__ import division
import time
import requests
import xlwt
import uuid
#  抓取阳光订单统计/小说统计的数据
headers = {
    'Referer': 'https://admin.yifengaf.cn/admin/collect/index?addtabs=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Cookie': 'PHPSESSID=2p6tlb5sv9268bu8mfidu85kg1; keeplogin=11930%7C604800%7C1573091758%7C6aef109cede8191800b1d1ae9048c468',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest'
}

html = requests.get('https://admin.yifengaf.cn/admin/collect/index?channel_id=0&sort=createdate&order=desc&offset=0&limit=31&_=1572329929049',headers=headers)
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
        "日期":i.get('createdate'),
        "PV":int(i.get('pv')),
        "UV": int(i.get('uv')),
        "总充值": float(i.get('recharge_money')),
        "普通充值(成功人次)": float(i.get("normal_recharge_orders")),  #"%s 成功人次:" %

        # format(float(i.get("noraml_recharge_guide_money"))/float(i.get("normal_recharge_orders")),'.2f'),   # 人均
       # int(float(i.get("noraml_recharge_guide_money"))),

        "普通充值订单数(已支付)": int(i.get("normal_recharge_orders")),
                                 # int(i.get("normal_recharge_orders_count")-i.get("normal_recharge_orders")),
                                 # '完成率:{:.0f}%'.format(i.get("normal_recharge_orders") / i.get("normal_recharge_orders_count") * 100),


        "年度VIP会员(成功人次)":
                                # float(i.get("vip_recharge_money")),
                                float(i.get("vip_recharge_orders")),

        # "年度VIP会员订单数": [
        #
        #
        #     int(i.get("vip_recharge_orders")),
        #     int(i.get("vip_recharge_orders_count")-i.get("vip_recharge_orders")),
        #     #  完成率 i.get("vip_recharge_orders")/i.get("vip_recharge_orders")
        # ],
        "充值": float(i.get('recharge_money')),
        "分成收益": float(i.get('total_benefit')),
        }
    jsonfile.append(dicts)
print(jsonfile)

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
    workbook.save('阳光平台%s.xls' % rd)


jsonToexcel()



