import os
import time

def Init_floder():
	floder_name = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	path = os.getcwd()+'\File'+'\{}'.format(floder_name)
	if os.path.exists(path):
		os.makedirs(path + '\Japanese')
		os.makedirs(path + '\Europe')
		os.makedirs(path + '\China')
	else:
		os.makedirs(path)
		os.makedirs(path + '\Japanese')
		os.makedirs(path + '\Europe')
		os.makedirs(path + '\China')

if __name__ == '__main__':
	print(Init_floder())