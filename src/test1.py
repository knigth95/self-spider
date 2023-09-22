#安装支持 解析 html 和xml的解析库  lxml
#pip  install lxml；xpath是一个语法，不是解析库
import requests
import re
from lxml import etree

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
url = 'http://news.baidu.com/'
data = requests.get(url,headers=headers).content.decode()
#print(data)
#1.转解析类型
xpath_data = etree.HTML(data)#将html文档或者xml文档转换成一个etree对象，然后调用对象中的方法查找指定的节点
#xpath 语法1.节点: /  2.跨节点:  //  3.精确的标签： //a[@属性=“属性值”] 4.标签包裹的内容:text()  5.属性：@href
#xpath返回的类型是list

#2.调用xpath的方法
# result = xpath_data.xpath('/html/head/title/text()')#'/'为根节点，不方便；输出：百度新闻——海量中文资讯平台
# result = xpath_data.xpath('//a/text()')#'//'为跨节点；取a标签包裹的内容
# result = xpath_data.xpath('//a[@mon="ct=1&c=top&a=30&pn=1"]/text()')# 精确的标签：//a[@属性=“属性值”]/text()
# result = xpath_data.xpath('//a[@mon="ct=1&c=top&a=30&pn=1"]/@href')#取出链接
print(len(result))
print(result)
