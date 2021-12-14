import json
import pandas as pd
from lxml import etree
from base_spider import BaseSpider
from utils import extract_first, is_file_exist


class DachengSpider(BaseSpider):
    def __init__(self):
        super().__init__()
        self.start_urls = [f"https://novel.tengwen.com/channel/index?page={i}" for i in range(1,13)]
        is_file_exist("qw.json")


    def get_data(self, resp):

        """取"""
        html = etree.HTML(resp)
        trs = html.xpath('//tbody/tr')
        datas = []
        # print(type(datas))
        for tr in trs:
            name = tr.xpath('./td[2]/div[1]/text()')    # 入口
            click = tr.xpath('./td[4]/a/text()')              #点击
            new_append = tr.xpath('./td[6]/text()')         # 新增关注
            recharge_amount = tr.xpath('./td[7]/text()')        #充值金额
            item = dict(
                name = extract_first(name),
                click=extract_first(click),
                new_append=extract_first(new_append),
                recharge_amount=extract_first(recharge_amount)
                # location=extract_first(location),
            )
            print(item)
            yield item

            # datas.append(item)

        # print(datas)
        # pf = pd.DataFrame(datas)
        #
        # # 指定字段顺序
        # order = ['name', 'click', 'new_append', 'recharge_amount']
        # pf = pf[order]
        # # 将列名替换为中文
        # columns_map = {
        #     'name': '路线',
        #     'click': '车牌',
        #     'new_append': '时间',
        #     'recharge_amount': '方向',
        # }
        # pf.rename(columns=columns_map, inplace=True)
        #
        # # 指定生成的Excel表格名称
        # file_path = pd.ExcelWriter('name.xlsx')
        # # 替换空单元格
        # pf.fillna(' ', inplace=True)
        # # 输出
        # pf.to_excel(file_path, encoding='utf-8', index=False)
        # # 保存表格
        # print(file_path.save())


        # df = pd.DataFrame(datas)  # 最后转换得到的结果
        # print(df)
        # df.to_excel('data.xls', sheet_name='Data', startcol=0, index=False)

        # return datas
        # print(len(trs))


    def save_data(self,data):

        with open("qw.json","a",encoding="utf8") as f:
            f.write(json.dumps(data,ensure_ascii=False)+",\n")
            # json.dump(data,f,ensure_ascii=False,indent=2)



    # def export_excel(self,export):
    #     # 将字典列表转换为DataFrame
    #     export = [{"name": "10.31-星阅11点客服", "click": "49", "new_append": "2", "recharge_amount": "￥ 0"}]
    #     # 将字典列表转换为DataFram
    #     pf = pd.DataFrame(list(export))
    #     # 指定字段顺序
    #     order = ['name', 'click', 'new_append', 'recharge_amount']
    #     pf = pf[order]
    #     # 将列名替换为中文
    #     columns_map = {
    #         'name': '路线',
    #         'click': '车牌',
    #         'new_append': '时间',
    #         'recharge_amount': '方向',
    #     }
    #     pf.rename(columns=columns_map, inplace=True)
    #     # 指定生成的Excel表格名称
    #     file_path = pd.ExcelWriter('name.xlsx')
    #     # 替换空单元格
    #     pf.fillna(' ', inplace=True)
    #     # 输出
    #     pf.to_excel(file_path, encoding='utf-8', index=False)
    #     # 保存表格
    #     file_path.save()


if __name__ == '__main__':
    spider = DachengSpider()
    spider.run()
