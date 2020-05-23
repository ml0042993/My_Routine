import time
from Core.Request_Site import Get_Request
from Core.Get_Time import Get_Time
from bs4 import BeautifulSoup
from Setting import Config
class Get_Eur(Get_Request):
	def __init__(self):
		super().__init__()
		self.page = Config.Europe_Url
		self.get_Html()
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
	def get_core_Result(self,url):
		'''
		获取相关链接内的标题,磁力链接,图片地址
		:param url: URL_POOL列表内获取的每个子页面的链接地址的集合
		:return:
		'''
		self.page = url
		self.get_Html()
		if self.respones != None:
			soup = BeautifulSoup(self.respones.text, 'lxml')
			title_message = soup.select('#thread_subject')[0].get_text()#获得标题
			print(title_message)
			magnet_message = soup.select('.blockcode li')[0].get_text()
			print(magnet_message)
			image_address = soup.select('.zoom')[0].attrs['file']#获取的第一个[0]图片的链接
			print(image_address)
	def get_Import_result(self):
		for url in self.URL_POOL:
			self.get_core_Result(url)
if __name__ == '__main__':
	obj = Get_Eur()
	obj.get_Url_Base()
	obj.get_Import_result()