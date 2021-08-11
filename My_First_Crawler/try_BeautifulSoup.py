from bs4 import BeautifulSoup

# convert html into a python tree like mdoel
file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# print(bs.title)#<title>百度一下，你就知道</title>
# print(bs.title.string)#百度一下，你就知道
# print(type(bs.title.string))#<class 'bs4.element.NavigableString'>
# print(bs.head)#只能拿到第一个head
# print(bs.a.attrs)#{'href': 'http://news.baidu.com', 'target': '_blank', 'class': ['mnav', 'c-font-normal', 'c-color-t']}
# print(type(bs))#BeautifulSoup: the whole file
# print(bs.a.string)#输出的内容不会包含注释、符号


# 遍历：
print(bs.head.contents[1])  # bs.head.contents返回一个列表

# 文档搜索：

# findall
# 字符串过滤：查找与字符串完全匹配的内容
# tlist=bs.find_all("a")

# 正则表达式搜索：使用search()方法来匹配内容
import re

t_list = bs.find_all(re.compile("a"))  # head 里面有个a，所以会显示head，只要是内容里面有a的全部匹配


# 传入函数。根据函数要求进行搜索
def name_is_exist(tag):
    return tag.has_attr("name")  # 返回所有包含name属性的标签


# t_list=bs.find_all(name_is_exist)


print(t_list)

# 使用参数进行查找
t_list = bs.find_all(id="head", class_=True, href="Http://www.baidu.com")

t_list = bs.find_all(text="hao123", limit=3)  # 拿出前三个
t_list = bs.find_all(text=re.compile("\d"))  # 找到所有text内包含数字的

# css选择器

print(bs.select('title'))
print(bs.select(".mnav"))  # 找出所有class为mnav的
print(bs.select("a[class='bri']"))
print(bs.select("head > div > div > title")) #head里面的div里面的div的title
# ~ 兄弟节点