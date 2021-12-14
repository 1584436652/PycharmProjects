import openpyxl as xl
import os
from lxml import etree
import requests


url = 'https://search.jd.com/Search?'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",

}
parems = {
    'keyword': 'iphone11',
    'suggest': '1.rem.0',
    'wq': 'iphone11',
    'pvid': '3e9eb35ab35a42a4afb77e2371813a83',
    'page': 2,
}
respones = requests.get(url = url,headers = headers,params=parems).text
print(respones)