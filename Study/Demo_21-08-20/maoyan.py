import requests
from retry import retry
from lxml import etree
from bs4 import BeautifulSoup

class Cat_Eye(object):

    def __init__(self):
        self.url = 'https://maoyan.com'
        self.verify_url = 'https://verify.maoyan.com/verify'
        self.first_url = 'https://maoyan.com/films'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                            '/91.0.4472.164 Safari/537.36',
            # 'cookie': '__mta=213868203.1629192172957.1629884589167.1629970158181.11; uuid_n_v=v1; _lxsdk_cuid=17b536bb518c8-0aae7e244245e5-6373260-1fa400-17b536bb518c8; _csrf=ca895f13c507d57f9c1fd3f6c2a3c5b7576bae773e0de9013ed7b519859f0461; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; uuid=5B6DD53006D811ECAE06094D3A36CA7B6172304D08674CC2BC8C618A29C65926; lt=9uWVxdZCIYs7qS29Muf8sbJhAokAAAAAbg4AAMFBw5AVq9gdCSbnB3gswcXdimJoxAOLD8EOx6GChTqRn3OlVgOVoAiJK44K1hKKNQ; lt.sig=n9dV4LT9f6hkfI8fkU1GdNxIk-w; uid=186775205; uid.sig=ZhX3Xt87E36Rh6tnlcrsEZYHiC8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1629943925,1629968447,1630028620,1630028685; _lxsdk=5B6DD53006D811ECAE06094D3A36CA7B6172304D08674CC2BC8C618A29C65926; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1630028750; __mta=213868203.1629192172957.1629970158181.1630028750613.12; _lxsdk_s=17b8546df11-996-e6-600%7C%7C13',
            # 'Host': 'maoyan.com',
            # 'Referer': 'https://maoyan.com/films',
            # 'sec-ch-ua-mobile': '?0',
            # 'Sec-Fetch-Dest': 'document',
            # 'Sec-Fetch-Mode': 'navigate',
            # 'Sec-Fetch-Site': 'same-origin',
            # 'Sec-Fetch-User': '?1',
            # 'Upgrade-Insecure-Requests': '1',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'Accept-Encoding': 'gzip,deflate,br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            # 'Connection': 'keep-alive'
        }

    @retry(delay=3, tries=3)
    def verification_url(self, url):
        print(f'{url}')
        try:
            res = requests.get(url=url, headers=self.headers)
            print(f"请求返回状态---{res.status_code}")
            res.encoding = 'utf-8'
            assert res.status_code == 200
            return res.text
        except Exception as e:
            raise e
            # return None

    def demo(self):
        url = self.verification_url(self.verify_url)
        print(url)

    """xpath获取url"""
    def get_home(self):
        url = self.first_url
        html_text = self.verification_url(url)
        html = etree.HTML(html_text)
        # print(html_text)
        a_label = html.xpath('//div[@class="channel-detail movie-item-title"]//a/@href')
        print("页面url长度：{}".format(len(a_label)))
        for i in a_label:
            join_str_url = "{}{}".format(self.url, i)
            yield join_str_url

    def movies_details(self, url):
        html_text = self.verification_url(url)
        html = etree.HTML(html_text)
        a_label = html.xpath('//div[@class="movie-brief-container"]//h1[@class="name"]//text()')
        print(a_label)

    """bs4获取url"""
    def get_home_bs4(self):
        html_text = self.verification_url()
        print(html_text)
        soup = BeautifulSoup(html_text, 'lxml')
        a = soup.findAll(name='_blank')
        print(a)
        for a_ in a:
            print(a_.get('href'))

    def main(self):
        cat.demo()
        movie_url = cat.get_home()
        for get_url in movie_url:
            cat.movies_details(get_url)

cat = Cat_Eye()
cat.main()
