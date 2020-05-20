import requests
from pyquery import PyQuery as pq
import setting

class Proxy_IP():
	def __init__(self):
		self.headers = setting.HEADERS
		self.URL_PROXY = []
		self.set_page()
		self.run()
	def set_page(self,page=1):
		self.Proxy_Site_Url = setting.Proxy_Site_Url+str(page)# 代理网站地址
		

	def get_Requsets(self):
		self.respones = requests.get(self.Proxy_Site_Url, headers=self.headers)
		if self.respones == None:
			print('Connect Fail')
			print('Try connecting again')

			self.get_Requsets()
		else:
			print("Connect Successful")

	def get_IP_Port(self):
		'''
		获取代理地址,未验证是否可用
		:return:
		'''
		html = self.respones.text
		doc = pq(html)
		doc.find('th').remove()  # 删除表头的节点
		dom = doc('table .country').parent()
		# print(dom)
		IP_address = list(dom('td:nth-child(2)').items())  # 返回的是一个生成器,需要变成list进行遍历
		Port_address = list(dom('td:nth-child(3)').items())
		Html_Type = list(dom('td:nth-child(6)').items())

		for i in range(len(IP_address)):
			# print(IP_address[i])
			URL_ADDRESS = '{}://{}:{}'.format(Html_Type[i].text(), IP_address[i].text(), Port_address[i].text())
			self.URL_PROXY.append(URL_ADDRESS)

	def run(self):
		self.get_Requsets()
		self.get_IP_Port()
if __name__ == '__main__':
	obj = Proxy_IP()

	for i in obj.URL_PROXY:
		print(i)