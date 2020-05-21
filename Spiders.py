import time
import requests
import setting
from Read_Proxy import random_proxy
class Get_Time():
	'''
	获取系统时间
	'''
	@staticmethod
	def TODAY_DATA():
		return time.strftime('%Y/%m/%d',time.localtime(time.time()))

# print(Get_Time.TODAY_DATA())
class Get_Request:
	def __init__(self):
		self.URL_POOL = []#符合条件的链接地址集合,通过列表内的地址进入各个页面,再爬取具体内容,链接池
		self.SITE_URL = setting.SITE_URL#主网址地址,用来和爬取的后半部分链接地址拼接为一个可用地址
		self.page = None
		self.headers = setting.HEADERS
	def get_Html(self):
		'''
		获取网页内容
		:param page:要爬取网页的内容
		:return:
		'''
		# print(page)
		proxy = random_proxy()
		# print(proxy)
		try:
			respones = requests.get(self.page,headers = self.headers,proxies=proxy,timeout=10)
			if respones:
				print("Connect Successful")
				self.respones = respones
			else:
				print('Connect Fail')
				print('Try connecting again')
				self.respones=None
		except requests.exceptions.InvalidSchema as e:
			self.respones = None
			print(e)

	def get_Url_Base(self):
		'''
		获取当天全部链接地址
		:return:
		'''
		pass
	def core_Result(self):
		'''
		根据获取的链接,获取需要爬取页面的html信息
		:return:
		'''
		pass
