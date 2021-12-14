import json

from lxml import etree

from base_spider import BaseSpider
from utils import extract_first, is_file_exist


class DachengSpider(BaseSpider):

    def __init__(self):
        super().__init__()
        self.start_urls = [f'https://cs.anjuke.com/sale/p{i}/#filtersort' for i in range(10)]
        is_file_exist("dacheng.json")



    def get_data(self, resp):
        """取"""
        html = etree.HTML(resp)
        trs = html.xpath('//ul[@id="houselist-mod-new"]')
        print(trs)
        datas = []
        for ul in trs:
            name = ul.xpath('./i/text()')
            location = ul.xpath('.//p[@class="name"]//text()')
            time = ul.xpath('.//p[@class="name"]/a/@href')
            type = ul.xpath('.//p[@class="star"]/text()')
            # chanquan = ul.xpath('.//p[@class="releasetime"]/text()')
            # huxin = ul.xpath('.//p[@class="score"]//text()')
            # large = ul.xpath('.//p[@class="score"]//text()')
            # turn = ul.xpath('.//p[@class="score"]//text()')
            # floor = ul.xpath('.//p[@class="score"]//text()')
            # lift = ul.xpath('.//p[@class="score"]//text()')
            # price_pre = ul.xpath('.//p[@class="score"]//text()')
            # price_sum = ul.xpath('.//p[@class="score"]//text()')
            # one_hand = ul.xpath('.//p[@class="score"]//text()')
            # zx_level = ul.xpath('.//p[@class="score"]//text()')
            item = dict(
                name = extract_first(name),
                location = extract_first(location),
                # "detail_url": "https://maoyan.com" + extract_first(time),
                time = extract_first(time),
                type = extract_first(type),
            )
                # "score": "".join(score),

            print(json.dumps(dict,ensure_ascii=False,skipkeys=False))
            yield dict

        # print(datas)



    def save_data(self,data):
        pass

        # with open("dacheng.json","a",encoding="utf8") as f:
        #     f.write(json.dumps(data,ensure_ascii=False)+",\n")
    #         # json.dump(data,f,ensure_ascii=False,indent=2)

if __name__ == '__main__':
    spider = DachengSpider()
    spider.run()
