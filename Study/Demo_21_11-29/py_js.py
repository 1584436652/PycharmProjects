import execjs
import Crypto
import time
import base64
import requests
from Crypto.Hash import SHA256, SHA1
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.Signature.pss import MGF1
from Crypto.PublicKey import RSA

s = requests.session()


def key():
    with open('js_code.js', 'r') as f:
        file = f.read()
    ctx = execjs.compile(file)
    result = ctx.call('o', "13677395742")
    print(result)


def pub_key(message):
    keys = """-----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDSovT1rrwzrGoMCFb6z8e+5lzVdAD5o8kr
    GIwdfxrVE2OnMijUZdkQk7etPJvZ2JOVXghthAGUUJkDUE8n2ZMNFKPjMrQJI49ewVzqWOKO
    vgU6Iu60Sn0xpeietP1wWXBkszdV1WfNBJUo2hhPDnIPMGzzdfLW5rMu+tczeUriJQIDAQAB
    -----END PUBLIC KEY-----
    """
    rsa_key = RSA.importKey(keys)
    cipher = PKCS1_v1_5.new(rsa_key)
    cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
    p_key = cipher_text.decode('utf-8')
    return p_key


def my_key():
    tm = round(time.time() * 1000)
    url = f"https://www.yuanfudao.com/tutor-ytk-account/accounts/api/login?" \
          f"_productId=374&_hostProductId=374&platform=www&version=5.11.0&" \
          f"YFD_U=488ff1abd92a740d6c8576d3f42e8f28&timestamp={tm}"
    url_message = f"https://www.yuanfudao.com/tutor-student-profile/api/users/current/summary?_productId=374&_hostProductId=374&platform=www&version=5.11.0&YFD_U=488ff1abd92a740d6c8576d3f42e8f28&timestamp={tm}"
    data = {
        "phone": pub_key("13677395742"),
        "password": pub_key("lkt02230330")
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    s.post(url, data=data, headers=headers)
    res = s.get(url_message, headers=headers)
    print(res.status_code)
    print(res.json())


my_key()

