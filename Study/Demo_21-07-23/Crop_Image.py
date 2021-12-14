from aip import AipOcr
import json
import requests


def get_img_url():
    word = input('请输入要爬取的关键字：')
    page = input('请输入要爬取多少页：')
    page = int(page) + 1
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    n = 0
    pn = 1
    # pn是从第几张图片获取 百度图片下滑时默认一次性显示30张
    for m in range(1, page):
        url = 'https://image.baidu.com/search/acjson?'

        param = {
            'tn': 'resultjson_com',
            'logid': '',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': word,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': word,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'force': '',
            'cg': 'girl',
            'pn': pn,  # 从第几张图片开始
            'rn': '30',
            'gsm': '1e',
        }
        page_text = requests.get(url=url, headers=header, params=param)
        page_text.encoding = 'utf-8'
        page_text = page_text.json()
        info_list = page_text['data']
        del info_list[-1]
        img_path_list = []
        for i in info_list:
            img_path_list.append(i['thumbURL'])

        for img_path in img_path_list:
            img_data = requests.get(url=img_path, headers=header).content
            img_path = './' + str(n) + '.jpg'
            # print(img_data)
            with open(img_path, "wb") as fp:
                fp.write(img_data)
            n = n + 1
        pn += 29


# def inte(filePath):
#     with open(filePath, "rb") as fp:
#         return fp.read()

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_license_plate(filePath):
    """ APPID AK SK """
    APP_ID = '24593385'
    API_KEY = 'f1CgWEQTkrZnroYrLlMIcppL'
    SECRET_KEY = 'Oi2PmKxW7lf8PsSH4Pga99LfQb2IoLcb'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(filePath)
    """ 调用车牌识别 """
    res = client.licensePlate(image)
    return res


if __name__ == '__main__':
    get_img_url()
    print("************")
    for i in range(16, 30):
        try:
            img_FilePath = "D:\\PycharmProjects\\Study\\Demo_21-07-23\\" + str(i) + '.jpg'   # 照片绝对地址
            # print(img_FilePath)
            res = get_license_plate(img_FilePath)
            print('车牌号码：' + res['words_result']['number'])
            print('车牌颜色：' + res['words_result']['color'])
            print("************")
            continue
        except:
            print('第' + str(i) + "个车牌有误")
            print("************")






