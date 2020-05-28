import aiohttp,asyncio
import time
from bs4 import BeautifulSoup
from Setting import Config
from Setting.Init_Floder import Floder_Create

class Original_Proxy():
	def __init__(self):
		pass
	async def get_Original_proxy(self,page):
		conn = aiohttp.TCPConnector(ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				async with session.get(page,timeout=10) as response:

					if response.status in Config.STATUS_CODES:
						self.response = await response.text()
						print(self.response)
					else:
						print("Error")
			except Exception as e:
				print(e)
				print("error")
				pass

	async def get_Url_IP(self):
		soup = BeautifulSoup(self.response, "lxml")

		for allmessage in soup.select('tbody tr'):
			# print(allmessage)
			ip = allmessage.select('td a')[0].get_text()
			port = allmessage.select('td')[1].get_text()
			if allmessage.select('td')[4].get_text() == "不支持":
				http = "http"
			else:
				http = "https"
			self.proxy = "{}://{}:{}".format(http, ip, port)

	def run_main(self):

		Floder_Create.create_Proxyfloder()
		original_path = Floder_Create().Original_path#创建首次获取的代理存放的文件及文件位置
		with open(original_path,'w') as f:
			try:
				loop = asyncio.get_event_loop()
				for i in range(0, len(Config.Proxy_Site_ihuan()), 10):
					valid_Url = Config.Proxy_Site_ihuan()[i:i + 10]
					# print(test_proxy)
					# for url in valid_Url:
					# 	task = self.get_Original_proxy(url)
					# 	tasks.append(task)
					tasks = [self.get_Original_proxy(Url) for Url in valid_Url]
					loop.run_until_complete(asyncio.wait(tasks))
					f.write(self.proxy)
					time.sleep(5)
			except Exception as e:
				print('xxxx')


if __name__ == '__main__':
	obj = Original_Proxy()
	obj.run_main()