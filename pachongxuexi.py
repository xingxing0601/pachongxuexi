# encoding=tuf-8
"""
前提知识：
    url
    http协议
    web前端，html.css.js
    ajax
    re,xpath
    xml

简介：
1，爬虫简介：
    定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常称为网页追逐者），
    是一种按照一定的规则，自动的抓取万维网信息的程序或者脚本。
    另外一些不常使用的名字：蚂蚁，自动索引，模拟程序，蠕虫

    两大特征：
        能按照作者要求下载数据或者内容
        能自动在网络上流窜

    三大步骤：
        下载网页；
        提取正确的信息
        根据一定的规则自动跳到另外的网页上执行上两部内容。

    爬虫分类
        通用爬虫
        专用爬虫（聚焦爬虫）
    python网络包简介
        python2.x：urllib,urllib2,urllib3,httplib,httplib2,requests; urllib和urllib2配合使用，或者requests
        python3.x:urllib,urllib3,httplib2,requests； urllib , requests

2.urllib
    包含模块
        urllib.requests:打开和读取urls
        urllib.error:包含urllib.requests产生的常见的错误，使用try捕捉.
        urllib.parse:包含解析url的方法
        urllib.robotparse：解析robots.txt文件
        代码：t001.py

    网络编码问题的解决(自动检测编码格式)：
        第三方包：可以自动检测页面文件的编码格式，但是可能有误。
        需要安装。conda install chardet
        代码：t002.py

    urlopen 的返回对象
        代码：t003.py
        geturl :返回请求对象的url
        info: 请求将反馈对象的meta信息
        getcode： 返回的http code

    request.data 的使用
        访问网络的两种方式：
        get
            利用参数给服务器传递信息
            参数为dict类型，然后用parse模块编码
            代码：t004.py
        post
            一般向服务器传递参数使用
            post是把信息自动加密处理
            如果想使用post信息，需要用到data参数
            使用post，意味着http的请求头可能需要更改
                content-type:
                content-length:参数长度
                一旦更改请求方法，请注意其他请求头部信息相适应
            urllib.parse.urlencode 可以将字符串自动转换成上面的。
            代码：t005.py(代码有问题，打不开)
            为了更多的设置请求信息，单纯的通过urlopen函数已经不太好用了
            需要利用request.Request类
            代码：t006.py

"""
