import urllib.request
import urllib.parse
#post
print("POSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
response=urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))

#get
print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
try:
    response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("Time out")

response=urllib.request.urlopen("http://httpbin.org/get")
print(response.status)
#200：成功
#418：发现是爬虫文件

req=urllib.request.Request