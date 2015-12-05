#encoding=utf-8
#功能：爬取贴吧上面的图片
import urllib2
import urllib
import re
#raw_input是python的一个内置函数，通过读取控制台的输入与用户实现交互。
#input也可以读取控制台的输入与用户实现交互，但是input和raw_input由一定的差异，
#例如：raw_input将控制台上所有的输入均作为字符串（即使全是数字组合）来进行处理，而input对输入有一定的要求，如果输入的是字符串，则一定要用引号
#从控制台输入一个url

#定义一个函数，得到内容
def getContent(content):
	#利用正则来进行匹配
	pattern=re.compile(r'src="(.*?)" alt=')
	items=re.findall(pattern,content)
	count=0
	for item in items:
		count+=1#python中没有++运算
		urllib.urlretrieve(item,"%s.jpg"  % count)

url=raw_input("raw_input:")
try:
	user_agent="Moizlla/5.0 (Windows NT/6.1)"
	headers={"User-Agent":user_agent}#请求头
	request=urllib2.Request(url,headers=headers)
	response=urllib2.urlopen(request)
	content=response.read()
	getContent(content)#调用getContent函数进行匹配
except urllib2.URLError,e:
	if hasattr(e,"reason"):
		print e.reason
