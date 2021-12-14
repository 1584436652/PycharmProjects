from openpyxl import workbook
import requests
from lxml import etree
# import openpyxl
import time


def get_greek(youbian_city):
    global ws
    for page in range(47454, 49270):
        url = f'https://{youbian_city}.postcodebase.com/zh-hans/node/{page}'
        # url = 'https://grc.postcodebase.com/zh-hans/node/1'
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
            # 'Referer': 'https://www.amazon.cn/s?i=stripbooks&fs=true&page=2',
            # 'Cookie': 'has_js=1; __utmc=131630094; __utmz=131630094.1627527654.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=131630094.2101535383.1627527654.1627539039.1627553951.4; __utmt=1; __utmb=131630094.2.10.1627553951',
            # 'referer': 'https: // grc.postcodebase.com/zh-hans/all?page = 0'
        }
        respones = requests.get(url=url, headers=headers)
        # zhuangtai= respones.status_code
        # print(zhuangtai)
        res = respones.text
        html = etree.HTML(res)
        postcode = []
        title = []
        city = []
        area_one = []
        area_two = []
        state = []
        html_data = html.xpath(f'//*[@id="node-{page}"]/div/div/fieldset[1]/div/div[2]/ul')
        # print(html_data)
        for gr in html_data:
            gr_postcode = gr.xpath('./li[6]/span[2]/span/text()')   # 邮编
            gr_title = gr.xpath('./li[1]/span[2]/span/text()')      # 标题
            gr_city = gr.xpath('./li[2]/span[2]/span/text()')  # 城市
            gr_area_one = gr.xpath('./li[4]/span[2]/span/a/text()')   # 区域1
            gr_area_two = gr.xpath('./li[3]/span[2]/span/a/text()')   # 区域2
            gr_state = gr.xpath('./li[5]/span[2]/span/text()')    # 国家
            print(gr_postcode, gr_title, gr_city, gr_area_one, gr_area_two, gr_state)

            for i in gr_postcode:
                postcode.append(i)
            for j in gr_title:
                title.append(j)
            for k in gr_city:
                city.append(k)
            for l in gr_area_one:
                area_one.append(l)
            for m in gr_area_two:
                area_two.append(m)
            for n in gr_state:
                state.append(n)

            for x in range(len(gr_postcode)):
                ws.append([postcode[x], title[x], city[x], area_one[x], area_two[x], state[x]])


if __name__ == '__main__':
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['邮编', '标题', '城市', '区域1', '区域2', '国家'])
    print("------xlsx-----")
    youbian_city = input("输入爬取的邮编国家（如：chn）：")
    get_greek(youbian_city)
    wb.save('xila.xlsx')
