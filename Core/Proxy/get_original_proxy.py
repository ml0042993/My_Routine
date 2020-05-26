from Core.Request_Site import Get_Request
from Setting import Config
class original_proxy(Get_Request):
	def __init__(self):
		super().__init__()
		self.SITE_URL = Config.Proxy_Site_Url_THREE
		self.proxy = None
	def run_main(self):
		for self.page in Config.Proxy_Site_Url_THREE_pagename:
			self.get_Html()