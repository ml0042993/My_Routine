import linecache
import random

def random_proxy():
	'''
	随机获取一个可用代理
	:return: 
	'''
	proxy_dic={}
	ran = random.randrange(1,5)

	proxy = linecache.getline(r'proxy_file',ran).replace('\n','')

	title = proxy.split('://')[0]
	proxy_dic[title] = proxy

	return proxy_dic
if __name__ == '__main__':
    
	print(random_proxy())
