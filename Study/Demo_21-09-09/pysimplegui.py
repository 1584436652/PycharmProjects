import requests


def show():
    url = 'https://private-amz.mabangerp.com/index.php?mod=stock.getStockList'
    show_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        # 'Host':'private-amz.mabangerp.com',
        'Cookie': 'gr_user_id=c2e3a8f2-5da2-424c-bad7-83447c138937; lang=cn; signed=1027914_0c443cab61a4d339bb4fdce449f9865e; MULTI_LANGUAGE_TYPE=%2BYjZ6oacL7xJ%2FKOcmBg9Z7cTOqi7UgOUgujRs4KQ4Ms%3D; Hm_lvt_2eaa3b6f220e8cc7a90ca518ff7ecf21=1632734871; Hm_lvt_b888e3a9116ee926400397d5e2c3792b=1631154936,1631791575,1632735176,1632794252; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ba94c97f4c44-0d933a597ad48e-c343365-2073600-17ba94c97f5583%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217ba94c97f4c44-0d933a597ad48e-c343365-2073600-17ba94c97f5583%22%7D; CRAWL_KANDENG_KEY=jRil5oghh2hoWRaFapsrA6y%2BJ3UfSX3dw%2BZOMq%2Fa8PMruiYtq9rGZj1heanwEWWMkCLnNWBONGEHELcPpDNGNQ%3D%3D; PHPSESSID=c1go9ogpe3k68p3tamf24uoum6; route=543c73aa82994c45ecbc531cb1f3435a'
    }
    sku_data = {
        'searchKey':'Stock_stockSku',
        'operate':'likeStart',
        'orderBys[]':'',
        'search-content':'库存SKU',
        'searchValue':'',
        'status':3,
        'parentCategoryId':'',
        'categoryId':'',
        'parentBrandId':'',
        'list-brandId':'',
        'labelId':'',
        'buyerId':'',
        'developerIdM':'',
        'artDesignerId':'',
        'salesId':'',
        'defaultStockWarehouseDetailId':'',
        'livenessType':'',
        'isNewType':'',
        'isMachining':'',
        'showstart':1,
        'isCloud':'',
        'isGift':'',
        'page':0,
        'rowsPerPage':100,
        'stockOrderby':'',
    }
    res1 = requests.post(url=url, headers=show_headers, data=sku_data)
    print(res1.cookies.get_dict())
    json_data = res1.json()["stockData"]
    for i in json_data:
        print(i.get("nameCN"))

show()
