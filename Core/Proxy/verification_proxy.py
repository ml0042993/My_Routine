import time
import os
import aiohttp,asyncio
from Setting import Config
from Core.Proxy.myProxy_IP import Proxy_IP
from Setting.Init_Floder import Floder_Create

class Verification(Proxy_IP):
	def __init__(self):
		super().__init__()
		self.SAVE_PROXY = []

	async def verif_URL(self,proxy):
		conn = aiohttp.TCPConnector(ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				start_time = time.time()
				async with session.get(Config.SITE_URL,proxy=proxy,timeout=5) as response:
					if response.status in Config.STATUS_CODES:
						end_time = time.time()
						self.SAVE_PROXY.append(proxy)
						print(end_time-start_time)

					else:
						print("Error")
			except Exception as e:
				# print("error")
				pass

	def main_Run(self):
		try:
			loop = asyncio.get_event_loop()
			for i in range(0,len(self.URL_PROXY),15):
				test_proxy = self.URL_PROXY[i:i+15]
				# print(test_proxy)
				tasks = [self.verif_URL(proxy) for proxy in test_proxy]
				loop.run_until_complete(asyncio.wait(tasks))
				time.sleep(5)
		except Exception as e:
			print('xxxx')

	def judge(self):
		flag = True
		page = 1
		while flag:
			self.run(page)
			print(self.Proxy_Site_Url)

			self.main_Run()
				# print(self.SAVE_PROXY)
			print("完成一次匹配")
			if len(self.SAVE_PROXY) >= 10 or page>9:
				break
			page+=1
	def write_File(self):
		filePath = Floder_Create().Proxy_path#建立proxy文件的路径
		print(os.path.exists(filePath))
		if Floder_Create().proxy_exist==False:#如果不存在
			Floder_Create.create_Proxyfloder()#创建该文件夹
		with open(filePath+'\proxy_file','w+') as fs:#打开proxy_file文件存放代理地址
			for result in self.SAVE_PROXY:
				fs.write(result+'\n')
	@property
	def Proxy_Total(self):
		return len(self.SAVE_PROXY)
if __name__ == '__main__':

	obj = Verification()
	obj.judge()
	obj.write_File()
	print(obj.Proxy_Total)
