import time
import requests
from bs4 import BeautifulSoup
class Get_Time():
	'''
	获取系统时间
	'''
	@staticmethod
	def TODAY_DATA():
		return time.strftime('%Y/%m/%d',time.localtime(time.time()))

# print(Get_Time.TODAY_DATA())
class get_request():
	def __init__(self):
		self.Japanese_Base = []#符合条件的链接地址集合,通过列表内的地址进入各个页面,再爬取具体内容
		self.Europe_Base = []#同上
		self.China_Base = []#同上

		self.Japanese_Url = "https://www.98asde.info/forum-103-1.html"
		self.Europe_Url = ''
		self.China_Url = ''

		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
		}
	def get_Html(self,page ="https://www.98asde.info/forum-103-1.html"):
		'''
		获取网页内容
		:param page:要爬取网页的内容
		:return:
		'''
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

	def Get_Url_Base(self):
		if self.respones != None:
			# print(self.respones.text)
			soup = BeautifulSoup(self.respones.text,'lxml')
			# soup = soup.prettify()
			for all_message in soup.select('tbody'):
				time_base = all_message.select('.by em span span')
				if len(time_base)>0:
					# print(time_base.attrs['title'])
					print(time_base)
					print(type(time_base))
				# if xxx:
				# 	print(xxx.select('em span span'))

		else:
			print('None')
if __name__ == '__main__':
	obj = get_request()
	obj.get_Html()
	obj.Get_Url_Base()