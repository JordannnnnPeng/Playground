import re

from bs4 import BeautifulSoup
import sys
import urllib.request
import xlwt


# for one url
def askURL(url):
    # User-Agent（用户代理）用于伪装，使服务器认为我是一个浏览器而非爬虫，同时也决定我们会收到什么样的东西
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}
    request = urllib.request.Request(url, headers=head)  # 访问
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        print("ERRORRRRRRRRRRRRRRRRRRRRRRR")
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(url):
    datalist = []

    return datalist


def savaData(savapath):
    return None


if __name__ == '__main__':
    url = "https://www.douban.com/doulist/2772079/?start=0&sort=seq&playable=0&sub_type="
    # 爬取网页
    for i in range(5):
        url_i = "https://www.douban.com/doulist/2772079/?start=" + str(i * 25) + "&sort=seq&playable=0&sub_type="
        html_i = askURL(url_i)
        # print(html_i)
        # 解析数据
        soup = BeautifulSoup(html_i, "html.parser")
        findlink = re.compile(r'<a href="(https://movie.douban.*?)" target="_blank">')
        findname = re.compile('>(?:\\s*)(.*)(?:\\s*)</a>(?:\\s*)</div>')  # 非捕获组和捕获组
        findabstract = re.compile('>(?:\\s*)(.*)(?:\\s*)<br/>(?:\\s*)(.*)(?:\\s*)<br/>(?:\\s*)(.*)(?:\\s*)<br/>')
        for item in soup.find_all('div', class_="bd doulist-subject"):  # 每个网页有25个，每次对其中的一个进行处理
            # print(item)
            data = []

            title = item.find_all(class_="title")
            abstract = item.find_all(class_="abstract")
            title = str(title)
            item = str(item)
            abstract = str(abstract)

            link = re.findall(findlink, item)[0]
            name = re.findall(findname, title)
            abstract_info = re.findall(findabstract, abstract)[0]
            data.append(name)
            data.append(link)
            data.append(abstract_info)
            print(data)

    # 保存数据
