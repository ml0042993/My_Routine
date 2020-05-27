from bs4 import BeautifulSoup
from Core.Request_Site import Get_Request
from Setting import Config
from Setting.Init_Floder import Floder_Create
class Original_Proxy(Get_Request):
	def __init__(self):
		super().__init__()
		self.SITE_URL = Config.Proxy_Site_Url_THREE
		self.proxy = None
	def run_main(self):

		Floder_Create.create_Proxyfloder()
		original_path = Floder_Create().Original_path#创建首次获取的代理存放的文件及文件位置
		with open(original_path,'w') as f:
			for title in Config.Proxy_Site_Url_THREE_pagename:

				self.page = Config.Proxy_Site_Url_THREE.format(title)
				print(self.page)
				self.proxy = None
				self.get_Html()
				soup = BeautifulSoup(self.respones.text,"lxml")

				for allmessage in soup.select('tbody tr'):
					# print(allmessage)
					ip = allmessage.select('td a')[0].get_text()
					port = allmessage.select('td')[1].get_text()
					if allmessage.select('td')[4].get_text() == "不支持":
						http="http"
					else:http = "https"
					proxy = "{}://{}:{}".format(http,ip,port)
					f.write(proxy)
					f.write("\n")
if __name__ == '__main__':
	obj = Original_Proxy()
	obj.run_main()