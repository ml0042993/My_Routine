import setting
import time
import aiohttp,asyncio
from myProxy_IP import Proxy_IP

class Verification(Proxy_IP):
	def __init__(self):
		super().__init__()
		self.SAVE_PROXY = []

	async def verif_URL(self,proxy):
		conn = aiohttp.TCPConnector(ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				start_time = time.time()
				async with session.get(setting.SITE_URL,proxy=proxy,timeout=15) as response:
					if response.status in setting.STATUS_CODES:
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
			if len(self.SAVE_PROXY) > 5 or page>5:
				break
			page+=1
	def write_File(self):
		with open('proxy_file','w+') as fs:
			for result in self.SAVE_PROXY:
				fs.write(result+'\n')
if __name__ == '__main__':

	obj = Verification()
	obj.judge()
	obj.write_File()

