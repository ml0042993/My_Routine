import time
class Get_Time():
	'''
	获取系统时间
	'''
	@staticmethod
	def TODAY_DATA():
		return time.strftime('%Y/%m/%d',time.localtime(time.time()))
