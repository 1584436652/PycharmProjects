import requests
import json
import re       #正则模块
import random   #随机数模块
import time

#query = 'python'
#读取之前登录后保存的cookies
with open('cookies.txt','r') as file:
    cookie = file.read()

url = 'https://mp.weixin.qq.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&share=1&token=773059916&lang=zh_CN',
    'Host': 'mp.weixin.qq.com',
}

cookies = json.loads(cookie)    #加载之前获取的cookies
print(cookies)     #可以打印看看，和之前保存的cookies是一样的

response = requests.get(url, cookies = cookies)    #请求https://mp.weixin.qq.com/,传cookies参数，登录成功
token = re.findall(r'token=(\d+)',str(response.url))[0]    #登录成功后，这是的url里是包含token的，要把token参数拿出来，方便后面构造data数据包发起post请求
#print(token)
#random.random()返回0到1之间随机数
#构造data数据包发起post请求
data = {
    'token': token,
    'lang': 'zh_CN',
    'f': 'json',
    'ajax': '1',
    'random': random.random(),
    'url': 'python',
    'begin': '0',
    'count': '3',
}

search_url = 'https://mp.weixin.qq.com/cgi-bin/operate_appmsg?sub=check_appmsg_copyright_stat'      #按F12在浏览器里找post请求的url（搜索文章请求的url）
search_response = requests.post(search_url, cookies=cookies, data=data, headers=headers)     #发起post请求，传cookies、data、headers参数
max_num = search_response.json().get('total')   #获取所有文章的条数
num = int(int(max_num/3)) #每页显示3篇文章，要翻total/3页，不过实际上我搜索了几个关键词，发现微信公众号文章搜索的接口最多显示667页，其实后面还有页数，max_num/3的结果大于667没关系

if __name__ == '__main__':
    query = input('请输入你要搜索的内容：')
begin = 0
while num +1 > 0:
    print(begin)
    data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'url': query,
        'begin': '{}'.format(str(begin)),
        'count': '3',
    }

    search_response = requests.post(search_url, cookies=cookies, data=data, headers=headers)

    contentt = search_response.json().get('list')               #list里面是我们需要的内容，所以要获取list

    for items in contentt:                                       #具体需要list里面的哪些参数可以自己选择，这里只获取title、url、nickname、author
        f = open('search.txt',mode='a',)                             #打开一个txt文档，把获取的内容写进去，mode='a'是追加的方式写入，不覆盖
        print('文章标题：',items.get('title'))  #获取文章标题
        f.write('文章标题：')
        f.write(items.get('title'))
        f.write("\n")
        f.write('文章url：')
        f.write(items.get('url'))
        f.write("\n")
        f.write('公众号：')
        f.write(items.get('nickname'))
        f.write("\n")
        f.write('作者：')
        f.write(items.get('author'))
        f.write("\n")
        f.write("\n")
        print('文章url：',items.get('url'))    #获取文章的url
        print('公众号：',items.get('nickname'))  #获取出自哪个微信公众号
        print('文章作者：',items.get('author'))   #获取文章作者

    num -= 1
    begin = int(begin)
    begin += 3
    time.sleep(3)