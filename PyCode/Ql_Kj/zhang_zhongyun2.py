import json
import pandas as pd
from lxml import etree
from base_spider import BaseSpider
from utils import extract_first, is_file_exist


class DachengSpider(BaseSpider):
    def __init__(self):
        super().__init__()
        self.start_urls = [f"https://inovel.818tu.com/backend/orders/index?status=1&per_page=20&page={i}" for i in range(1, 4)]
        is_file_exist("zhang_zhyun.json")

    def get_data(self, resp):
        """取"""
        html = etree.HTML(resp)
        trs = html.xpath('//tbody/tr')
        datas = []
        # print(type(datas))
        for tr in trs:
            name = tr.xpath('./td[2]/div/span[1]/text()')    # 用户id
            click = tr.xpath('./td[4]/text()')              # 累计充值
            money = tr.xpath('./td[7]/span/text()')        # 金额
            zhuangtai = tr.xpath('./td[8]/span/text()')        # 订单状态
            new_append = tr.xpath('./td[9]/text()')       # 创建时间
            book = tr.xpath('./td[10]/a/tex t()')             # 来源小说
            recharge_amount = tr.xpath('./td[11]/text()')        #来源链接
            item = dict(
                name = extract_first(name),
                click=extract_first(click),
                money=extract_first(money),
                zhuangtai=extract_first(zhuangtai),
                new_append=extract_first(new_append),
                book=extract_first(book),
                recharge_amount=extract_first(recharge_amount)
                # location=extract_first(location),
            )
            print(item)
            yield item


    def save_data(self,data):

        with open("zhang_zhyun.json", "a", encoding="utf8") as f:
            f.write(json.dumps(data, ensure_ascii=False)+",\n")
            # json.dump(data,f,ensure_ascii=False,indent=2)


if __name__ == '__main__':

    spider = DachengSpider()
    spider.run()
