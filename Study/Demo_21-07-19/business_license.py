import requests
import base64
import requests
'''
营业执照识别
'''


# client_id 为官网获取的AK， client_secret 为官网获取的SK
def get_access_token():
    access_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
                       '&client_id=DVOep9tBuMwb20bvGDd4erBY&client_secret=tTrGGnTnGnuwAEZY4DQGNMUsKRETRYUD'
    response = requests.get(access_token_url)
    if response:
        return response.json()["access_token"]


def recognition(img_path, access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/business_license"
    # 二进制方式打开图片文件
    with open(img_path, 'rb') as f:
        img = base64.b64encode(f.read())
    params = {"image":img}
    access_token = access_token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())


token = get_access_token()
recognition('安吉蓝城电子商务有限公司.jpeg', token)