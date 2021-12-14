from aip import AipOcr


def baidu_recognition(img_paths):
    """
    百度api执行所需数据，运行需换成自己的APP_ID，API_KEY，SECRET_KEY
    :param img_paths: 图片地址
    :return:
    """
    app_id = '24595087'
    api_key = 'A9Dqch23gVtuPBfXmBeVGfoE'
    secret_key = 'qm5p1RwwzZBrgaXG5C4GbCKM2BMhgjwP'
    # 初始化AipOcr
    aip_ocr = AipOcr(app_id, api_key, secret_key)
    with open(img_path, 'rb') as f:
        img2 = f.read()
    # print(type(img2))
    # 识别图片并返回结果
    result = aip_ocr.basicAccurate(img2)
    return result


def parse_picture(binary_data):
    """
    解析识别的翻译文本
    :param binary_data:
    :return:
    """
    words_result = binary_data["words_result"]
    for data in words_result:
        print(data)


if __name__ == '__main__':
    # img_path = r'C:\Users\Administrator\Desktop\营业执照\苍南县翎翎电子商务有限公司.jpeg'
    img_path = r'C:\Users\Administrator\Desktop\2.jpg'
    binary = baidu_recognition(img_path)
    parse_picture(binary)


