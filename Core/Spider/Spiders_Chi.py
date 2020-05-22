import time
from Core.Request_Site import Get_Request
from Core.Get_Time import Get_Time
from bs4 import BeautifulSoup
from Setting import Config

class Get_Chi(Get_Request):
	def __init__(self):
		super().__init__()
		self.page = Config.China_Url
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
	def core_Result(self):
		for url in self.URL_POOL:
			self.page=url
			self.get_Html()
			if self.respones != None:
				# print(self.respones.text)
				soup = BeautifulSoup(self.respones.text, 'lxml')
				# print(soup.prettify())
				title_message = soup.select('#thread_subject')[0].get_text()#获得标题
					# aaa = all_message.select('#thread_subject')
				print(title_message)
				magnet_message = soup.select('.blockcode li')[0].get_text()
				print(magnet_message)
				image_address = soup.select('.zoom')[0].attrs['file']
				print(image_address)

if __name__ == '__main__':
	obj = Get_Chi()
	obj.get_Url_Base()
	obj.core_Result()