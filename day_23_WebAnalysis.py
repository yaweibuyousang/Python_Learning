#从Web解析到网络空间
'''
Python库之网络爬虫
Python库之Web信息提取
Python库之Web网站开发
Python库之网络应用开发


Python库之网络爬虫
Requests:最友好的网络爬虫功能库
提供了简单易用的类HTTP协议网络爬虫功能
支持链接池，SSL，Cookies，HTTP(S)代理等
Python最主要的页面级网络爬虫功能库

import requests
r = requests.get('https://api.github.com/user',\
                auth=('user','pass'))
r.status_code
r.headers['content-type']
t.encoding
t.text


Scrapy:优秀的网络爬虫
提供了构建网络爬虫系统的框架功能，功能半成品
支持批量和定时网页爬取，提供数据处理流程等
Python最主要且最专业的网络爬虫框架

pyspider:强大的Web网页爬取系统
提供了完整的网页爬取系统构建功能
支持数据库后端，消息队列，优先级，分布式架构等
Python重要的网络爬虫类第三方库

Python库之Web信息提取
Beautiful Soup:HTML和XML的解析库
提供了解析HTML和XML等Web信息的功能
又名beautifulsoup4或bs4，可以加载多种解析引擎
常与网络爬虫库搭配使用，如Scrapy，requests等

Re:正则表达式解析和处理功能库
提供了定义和解析正则表达式的一批通用功能
可用于各类场景，包括定点的Web信息提取
Python最主要的标准库之一，无需安装

eg:
re.search()
re.split()
re.match()
re.finditer()
re.findall()
re.sub()
r'\d{3}-\d{8}|\d{4}-\d{7}'

Python-Goose:提取文章类型Web页面的功能库
提供了对Web页面中文章信息/视频等元数据的提取功能
针对特定类型Web页面，应用覆盖面较广
Python最主要的Web信息提取库

eg:
from goose import Goose
url = 'http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html'
g = Goose({'use_meta_language':False,'target_language':'es'})
article = g.extract(url=url)
article.cleaned_text[:150]

Django:最流行的Web应用框架
提供了构建Web系统的基本应用框架
MTV模式:模型(model)，模板(Template),视图(views)
Python最重要的Web应用框架，略显复杂的应用框架

Pyramid:规模适中的Web应用框架
提供了简单方便构建Web系统的应用框架
不大不小，规模适中，适合快速构建并适度扩展类应用
Python产品级Web应用框架，起步简单可扩展性好

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hell_world(requesr):
    return Response('Hello world!')
if __name__ == '__main__';
    with Configurator() as config:
        config.add('hello','/')
        config.add_view(hello,route_name('hello'))
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0',6543,app)
    server.server_forever()


Flask:Web应用开发微框架
提供了最简单构建Web系统的应用框架
特点是简单，规模小，快速
Django>Pramid>Flask

eg:
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello,World!'

WeRoBot:微信公众号开发框架
提供了解析微信服务器消息及反馈消息的功能
建立微信机器人的重要技术手段

aip:百度AI开放平台接口
提供了访问百度AI服务的Python功能接口
语音，人脸，OCR，NLP，只是图谱，图像搜索等领域
Python百度AI应用的最主要方式

MyQR:二维码生成第三方库
提供了生成二维码的系列功能
基本二维码，艺术二维码，动态二维码


'''
