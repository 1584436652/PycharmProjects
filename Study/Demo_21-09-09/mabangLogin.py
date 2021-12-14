'''
@Time    : 2021/9/27 15:09
@Author  : LKT
@FileName: mabangLogin.py
@Software: PyCharm
 
'''
import json
import requests
import http.cookiejar as ck

my_session = requests.session()
my_session.cookies = ck.LWPCookieJar(filename = "Cookies.txt")


def login(username, password):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Accept': 'application/json,text/javascript,*/*;q=0.01'

    }

    login_url = 'https://900539.private.mabangerp.com/index.php?mod=main.doLogin'
    login_data = {
        "isMallRpcFinds": "",
        "username": username,
        "password": password,
    }
    # proxies = {
    #            'https': '223.244.179.116:3256'
    #
    url1 = 'https://900539.private.mabangerp.com/index.htm'
    a = my_session.get(url1, headers=headers)
    res = my_session.post(url=login_url, headers=headers, data=login_data)
    # res.encoding = 'utf-8'

    print(res.text)
    my_session.cookies.save()
    # sku_data = {
    #     'searchKey': 'Stock_stockSku',
    #     'operate': 'likeStart',
    #     'orderBys[]': '',
    #     'search-content': '库存SKU',
    #     'searchValue': '',
    #     'status': 3,
    #     'parentCategoryId': '',
    #     'categoryId': '',
    #     'parentBrandId': '',
    #     'list-brandId': '',
    #     'labelId': '',
    #     'buyerId': '',
    #     'developerIdM': '',
    #     'artDesignerId': '',
    #     'salesId': '',
    #     'defaultStockWarehouseDetailId': '',
    #     'livenessType': '',
    #     'isNewType': '',
    #     'isMachining': '',
    #     'showstart': 1,
    #     'isCloud': '',
    #     'isGift': '',
    #     'page': 0,
    #     'rowsPerPage': 100,
    #     'stockOrderby': '',
    # }
    # url_sku = 'https://900539.private.mabangerp.com/index.php?mod=order.list&Order_orderStatus=2'
    # res2 = my_session.get(url=url_sku, headers=headers)
    # print('*/////////////')
    # print(res2.text)

# input_username = input("账号：")
# input_password = input("密码：")
if __name__ == "__main__":
    login("13677395742", "d6qE37SZ")






