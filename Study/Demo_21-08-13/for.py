import requests
from lxml import etree



def get_url():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0'
                      '.4472.164 Safari/537.36'}
    url = 'https://www.landchina.com/default.aspx?tabid=226'
    res = requests.get(url= url, headers = headers)
    res_code = res.status_code
    if res_code == 200:
        print("请求成功")
        data = []
        html = res.text
        html_text = etree.HTML(html)
        father_html = html_text.xpath('//table[@id="TAB_contentTable"]')
        for i in father_html:
            number = i.xpath('//td[@class="gridTdNumber"]/text()')
            region = i.xpath('//td[@class="queryCellBordy"][1]/text()')
            time = i.xpath('//td[@class="queryCellBordy"][3]/text()')
            title = i.xpath('//td[@class="queryCellBordy"][2]//a/text()')
            data.append(number)
            item = dict(
                序号=number,
                行政区=region,
                标题=title,
                日期=time
            )
            # yield item
            print(item)
            return item


def str_dispose(self, str_text:list):
    if str_text and str_text[0]:
        return str_text[0].strip()
    return None



save()