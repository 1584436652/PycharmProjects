import time
import asyncio
import aiohttp
import requests
from retry import retry
from lxml import etree
from typing import List


URL = [f"http://bbs.huoying666.com/forum.php?mod=forumdisplay&fid=53&typeid=2&typeid=2&filter=typeid&page={page}" for page in range(1, 11)]


class WallpaperRequest:

    def __init__(self):
        self.headers = {
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Referer': 'http://bbs.huoying666.com/forum-53-1.html',
        }

    @retry(tries=3, delay=3)
    def fetch(self, url):
        resp = requests.get(url=url, headers=self.headers)
        assert resp.status_code == 200
        return resp

    async def aio_download_read(self, url):
        """
        read()
        """
        async with aiohttp.ClientSession() as s:
            res = await s.get(url, headers=self.headers)
            return await res.read()
        
    async def aio_download_text(self, url):
        """
        text()
        """
        async with aiohttp.ClientSession() as s:
            res = await s.get(url, headers=self.headers)
            return await res.text()


class WallpaperParse:

    @classmethod
    def parse(cls, response):
        resp_text = response.text
        html = etree.HTML(resp_text)
        items = html.xpath('//ul[@id="waterfall1"]/li')
        https = "http://bbs.huoying666.com/"
        for item in items:
            w_title = item.xpath('./div[@class="auth cl"]/h3/a/text()')[0]
            w_link = https + item.xpath('./div[@class="auth cl"]/h3/a/@href')[0]
            # print(w_title, w_link)
            yield {
                "title": w_title,
                "link": w_link
            }

    @classmethod
    def detail_parse(cls, response):
        # resp_text = response.text()
        html = etree.HTML(response)
        items = html.xpath('//td[@class="t_f"]/font/a/@href')
        if items:
            return items[0]
        return html.xpath('//td[@class="t_f"]/a/@href')[0]


class SaveMov:

    def __init__(self, filename, file):
        with open(filename, 'wb') as fp:
            fp.write(file)


async def aio_file_save(filename, file):
    pass


def main():
    req = WallpaperRequest().fetch(URL[0])
    for data in WallpaperParse.parse(req):
        req_d = WallpaperRequest().fetch(data["link"])
        mov = WallpaperParse.detail_parse(req_d)
        print(f'爬取 {mov} ing.....')
        req_m = WallpaperRequest().fetch(mov)
        mov_f = req_m.content
        SaveMov(f"./wall/{data['title']}.mov", mov_f)
        time.sleep(1)


def main_asy():
    req = WallpaperRequest().fetch(URL[0])
    ulr_mov = []
    look = asyncio.get_event_loop()
    for data in WallpaperParse.parse(req):
        req_d = WallpaperRequest().aio_download_text(data["link"])
        page_url = look.run_until_complete(req_d)
        mov = WallpaperParse.detail_parse(page_url)
        print(f'{mov} ing.....')
        ulr_mov.append(mov)
    task = [WallpaperRequest().aio_download_read(url) for url in ulr_mov]
    tasks = asyncio.gather(*task)
    print(task)
    look.run_until_complete(tasks)


if __name__ == '__main__':
    main_asy()