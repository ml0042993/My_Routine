import setting
import time
import aiohttp,asyncio
from myProxy_IP import Proxy_IP

class Verification(Proxy_IP):
	def __init__(self):
		super().__init__()
		self.SAVE_PROXY = []

	async def verif_URL(self,proxy):
		conn = aiohttp.TCPConnector(verify_ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				async with session.get('https://www.baidu.com',proxy=proxy,timeout=15) as response:
					if response.status in setting.STATUS_CODES:
						self.SAVE_PROXY.append(proxy)
					else:
						print("Error")
			except Exception as e:
				print("error")

	def main_Run(self):
		try:
			loop = asyncio.get_event_loop()
			for i in range(0,len(self.URL_PROXY),100):
				test_proxy = self.URL_PROXY[i:i+100]
				print(test_proxy)
				tasks = [self.verif_URL(proxy) for proxy in test_proxy]
				loop.run_until_complete(asyncio.wait(tasks))
				time.sleep(5)
		except Exception as e:
			print('xxxx')

	def judge(self):
		flag = True
		page = 1
		while flag:
			self.set_page(page)
			self.main_Run()
			print(self.Proxy_Site_Url)
			if len(self.SAVE_PROXY) > 5:
				break
			page+=1
obj = Verification()
obj.judge()

print(obj.SAVE_PROXY)