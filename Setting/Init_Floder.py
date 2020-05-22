import os
import time

class Floder_Create:
	def __init__(self):
		self.get_Parent_path()
		self.get_Proxy_path()
		self.get_File_path()

	def get_Parent_path(self):
		'''
		获取根目录地址
		:return:
		'''
		path = os.path.dirname(__file__)#获取当前目录
		self.parent_path = os.path.dirname(path)#获取上级目录
	def get_Proxy_path(self):
		'''
		创建代理文件夹路径
		:return:
		'''
		self.proxy_Path =self.parent_path + '\File\Proxy'
	def get_File_path(self):
		'''
		创建文件存放的文件夹路径
		:return:
		'''
		floder_name = time.strftime('%Y-%m-%d',time.localtime(time.time()))#获取当天日期作为文件名
		self.file_Path = self.parent_path + '\File' + '\{}'.format(floder_name)#File下创建一个以当天时间为名称的文件夹

	@property
	def Parent_path(self):
		return self.parent_path
	@property
	def Proxy_path(self):
		return self.proxy_Path
	@property
	def File_path(self):
		return self.file_Path

	def creat_File_floder(self):
		'''
		生成文件存放的文件夹位置
		:return:
		'''
		try:
			if os.path.exists(self.file_Path):#判断路径是否存在
				return True
			else:
				os.makedirs(self.file_Path)
				os.makedirs(self.file_Path + '\Japanese')
				os.makedirs(self.file_Path + '\Europe')
				os.makedirs(self.file_Path + '\China')
		except FileExistsError as e:
			print(e)
			pass

	def create_Proxy_floder(self):
		'''
		创建代理文件存放的文件夹
		:return:
		'''
		try:
			if os.path.exists(self.proxy_Path):
				return True
			else:
				os.makedirs(self.proxy_Path)
		except FileExistsError as e:
			print(e)

	@classmethod
	def create_Proxyfloder(cls):
		'''
		调用create_Proxy_floder()使其成为类属性,方便调用
		:return:
		'''
		return cls().create_Proxy_floder()

