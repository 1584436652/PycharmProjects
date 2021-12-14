import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    # 对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'http://www.shicimingju.com/book/shijing.html'
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = 'utf-8'
    data = page_text.text
    # 在首页中解析出章节的标题和详情页的url
    # 实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(data, 'lxml')
    # 解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')

    fp = open('./sanguo.html', 'w', encoding='utf8')
    # with open('./sanguo.txt', 'w', encoding='utf8') as fp:
    #     fp.write(str(li_list))
    #     print(li_list)
    for li in li_list:
        title = li.a.string
        # print(title)
        detail_url = 'http://www.shicimingju.com'+li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers)
        detail_page_text.encoding = 'utf-8'
        data1 = detail_page_text.text
        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(data1, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title, '爬取成功！！！')
    fp.close()