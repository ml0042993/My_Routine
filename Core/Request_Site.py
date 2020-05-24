import requests
from Setting import Config
from Core.Read_Proxy import random_proxy
from Setting.Init_Floder import Floder_Create
from requests.exceptions import ConnectionError, ReadTimeout
class Get_Request:
	def __init__(self):
		self.URL_POOL = []#符合条件的链接地址集合,通过列表内的地址进入各个页面,再爬取具体内容,链接池
		self.SITE_URL = Config.SITE_URL#主网址地址,用来和爬取的后半部分链接地址拼接为一个可用地址
		self.creat_floder()
		self.page = None
		self.headers = Config.HEADERS
		self.get_Proxy()

	def get_Html(self):
		'''
		获取网页内容
		:param page:要爬取网页的内容
		:return:
		'''
		print(self.proxy)
		try:
			respones = requests.get(self.page,headers = self.headers,proxies=self.proxy,timeout=20)
			if respones:
				print("Connect Successful")
				self.respones = respones
			else:
				print('Connect Fail')
				print('Try connecting again')
				self.respones=None
		except ConnectionError as e:#当网络没有响应时
			self.respones = None
			self.get_Proxy()#更换代理
			self.get_Html()#重新获取response
			print(e)
	def get_image(self):
		'''
		获取网页内容
		:param page:要爬取网页的内容
		:return:
		'''
		print(self.proxy)
		try:
			respones = requests.get(self.page,headers = self.headers,timeout=20)
			if respones:
				print("Connect Successful")
				self.respones = respones
			else:
				print('Connect Fail')
				print('Try connecting again')
				self.respones=None
		except ConnectionError as e:#当网络没有响应时
			self.respones = None
			self.get_Html()#重新获取response
			print(e)
	def get_Proxy(self):
		if Floder_Create().proxy_exist:
			self.proxy=None
			self.proxy = random_proxy()

	def get_Url_Base(self):
		'''
		获取当天全部链接地址
		:return:
		'''
		pass
	def get_core_Result(self,url):
		'''
		根据获取的链接,获取需要爬取页面的html信息
		获取相关链接内的标题,磁力链接,图片地址
		:return:
		'''
		pass
	def creat_floder(self):
		Floder_Create.create_Filefloder()

	def save_Image(self):
		pass

'''
IOError
 +-- RequestException  # 处理不确定的异常请求
      +-- HTTPError  # HTTP错误
      +-- ConnectionError  # 连接错误
      |    +-- ProxyError  # 代理错误
      |    +-- SSLError  # SSL错误
      |    +-- ConnectTimeout(+-- Timeout)  # (双重继承，下同)尝试连接到远程服务器时请求超时，产生此错误的请求可以安全地重试。
      +-- Timeout  # 请求超时
      |    +-- ReadTimeout  # 服务器未在指定的时间内发送任何数据
      +-- URLRequired  # 发出请求需要有效的URL
      +-- TooManyRedirects  # 重定向太多
      +-- MissingSchema(+-- ValueError) # 缺少URL架构(例如http或https)
      +-- InvalidSchema(+-- ValueError) # 无效的架构，有效架构请参见defaults.py
      +-- InvalidURL(+-- ValueError)  # 无效的URL
      |    +-- InvalidProxyURL  # 无效的代理URL
      +-- InvalidHeader(+-- ValueError)  # 无效的Header
      +-- ChunkedEncodingError  # 服务器声明了chunked编码但发送了一个无效的chunk
      +-- ContentDecodingError(+-- BaseHTTPError)  # 无法解码响应内容
      +-- StreamConsumedError(+-- TypeError)  # 此响应的内容已被使用
      +-- RetryError  # 自定义重试逻辑失败
      +-- UnrewindableBodyError  # 尝试倒回正文时，请求遇到错误
      +-- FileModeWarning(+-- DeprecationWarning)  # 文件以文本模式打开，但Requests确定其二进制长度
      +-- RequestsDependencyWarning  # 导入的依赖项与预期的版本范围不匹配
 
Warning
 +-- RequestsWarning  # 请求的基本警告
'''