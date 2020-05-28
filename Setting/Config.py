#网站地址
SITE_URL = 'https://www.98asde.info/'#
Japanese_Url = "https://www.98asde.info/forum-103-1.html"
Europe_Url = 'https://www.98asde.info/forum-38-1.html'
China_Url = 'https://www.98asde.info/forum-2-1.html'
Proxy_Site_Url_ONE = "https://www.xicidaili.com/nn/"  # 代理网站地址
# Proxy_Site_Url_ONE = "https://www.xicidaili.com/nt/"  # 代理网站地址
Proxy_Site_Url_TOW = "https://ip.jiangxianli.com/?page={page}&anonymity=2"  # 代理网站地址
Proxy_Site_Url_ihuan = 'https://ip.ihuan.me/anonymity/2.html?page={}'
Proxy_Site_Url_ihuan_pagename = ["b97827cc","4ce63706","5crfe930","f3k1d581","ce1d45977","881aaf7b5","eas7a436","981o917f5","2d28bd81a","a42g5985d","came0299","e92k59727",
		 "242r0e7b5","bc265a560","622b6a5d3","ae3g7e7aa","b01j07395","68141a2df","904545743","0134c4568"]
#请求头
HEADERS = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
		}

STATUS_CODES = [200]

def Proxy_Site_ihuan():
	valid_Url=[]
	for pageend in Proxy_Site_Url_ihuan_pagename:
		Url = Proxy_Site_Url_ihuan.format(pageend)
		valid_Url.append(Url)
	return valid_Url

if __name__ == '__main__':
	for i in Proxy_Site_ihuan():
		print(i)