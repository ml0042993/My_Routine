import linecache
import random
import os
from Setting.Init_Floder import Floder_Create

def random_proxy():
	'''
	随机获取一个可用代理i
	:return: 
	'''
	filePath = Floder_Create().Proxy_path+'\proxy_file'  # 建立proxy文件的路径
	if os.path.exists(filePath):
		proxy_dic={}
		count = len(open(filePath,'r').readlines())

		ran = random.randrange(1,count)

		proxy = linecache.getline(filePath,ran).replace('\n','')

		title = proxy.split('://')[0]
		proxy_dic[title] = proxy

		return proxy_dic
	else:
		print('No path')
if __name__ == '__main__':
    
	print(random_proxy())
