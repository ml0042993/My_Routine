import time
import requests
from bs4 import BeautifulSoup
import setting
class Get_Time():
	'''
	获取系统时间
	'''
	@staticmethod
	def TODAY_DATA():
		return time.strftime('%Y/%m/%d',time.localtime(time.time()))

# print(Get_Time.TODAY_DATA())
class Get_Request():
	def __init__(self):
		self.URL_POOL = []#符合条件的链接地址集合,通过列表内的地址进入各个页面,再爬取具体内容,链接池

		self.SITE_URL = setting.SITE_URL#主网址地址,用来和爬取的后半部分链接地址拼接为一个可用地址

		self.Japanese_Url = setting.Japanese_Url
		self.Europe_Url = ''
		self.China_Url = ''

		self.headers = setting.HEADERS
	def get_Html(self,page ="https://www.98asde.info/forum-103-1.html"):
		'''
		获取网页内容
		:param page:要爬取网页的内容
		:return:
		'''
		print(page)
		try:
			respones = requests.get(page,headers = self.headers,timeout=10)
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
		if self.respones != None:
			# print(self.respones.text)
			soup = BeautifulSoup(self.respones.text,'lxml')
			# soup = soup.prettify()
			for all_message in soup.select('tbody'):
				time_base = all_message.select('.by em span span')#定位到每个链接的发布日期,time_base是一个列表,内部元素是Tag类型节点
				if len(time_base)>0:
					TIME_DATA = time_base[0].attrs['title']#得到发布时间是一个str
					if time.strptime(Get_Time.TODAY_DATA(),'%Y/%m/%d')==time.strptime(TIME_DATA,'%Y-%m-%d'):#判断是否是当天时间
						HARF_URL = all_message.select('.icn a')[0].attrs['href']#thread-340374-1-1.html,得到后半部分链接
						ALL_URL = self.SITE_URL+HARF_URL
						self.URL_POOL.append(ALL_URL)
		else:
			print('None')
	def core_Result(self):
		# for url in self.URL_POOL:
		self.get_Html(self.URL_POOL[0])
		if self.respones != None:
			# print(self.respones.text)
			soup = BeautifulSoup(self.respones.text, 'lxml')
			print(soup.prettify())
			for all_message in soup.select('table tbody h1'):
				print(all_message.text)


if __name__ == '__main__':
	obj = Get_Request()
	obj.get_Html()
	obj.get_Url_Base()
	obj.core_Result()
