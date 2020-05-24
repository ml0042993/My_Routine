import time
import json
from Core.Request_Site import Get_Request
from Core.Get_Time import Get_Time
from bs4 import BeautifulSoup
from Setting import Config
from Setting.Init_Floder import Floder_Create
from Core.Get_File import Get_File
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
						ALL_URL = self.SITE_URL+HARF_URL#拼接完整链接地址
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
			self.title_message = soup.select('#thread_subject')[0].get_text()#获得标题
			print(self.title_message)
			self.magnet_message = soup.select('.blockcode li')[0].get_text()
			print(self.magnet_message)
			self.image_address = soup.select('.zoom')[0].attrs['file']#获取的第一个[0]图片的链接
			print(self.image_address)
	def get_Import_result(self):
		file_path = Floder_Create().File_path + '\China'
		with open(file_path+'\File','w',encoding='utf-8') as f:
			for i in range(len(self.URL_POOL)):
				file_result = {}
				self.get_core_Result(self.URL_POOL[i])
				imagesave_path = Floder_Create().chi_image_path+"\%03d"%(i+1)

				Get_File.run_Image(self.image_address,imagesave_path)
				file_result['title'] = self.title_message
				file_result['magnet'] = self.magnet_message
				file_result['image'] = imagesave_path
				file_result = json.dumps(file_result)
				print(file_result)
				f.write(file_result+'\n')

	def run_chisite(self):
		self.get_Url_Base()
		self.get_Import_result()
if __name__ == '__main__':
	obj = Get_Chi()
	obj.get_Url_Base()
	obj.get_Import_result()