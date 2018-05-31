# search google for proxy servers and copy ip address and port number

import sys

if sys.version_info[0]==2:
        #for python 2
	import urllib
	proxy={'http':'http://138.122.2.7:53281'}
	print('without proxy:\n')
	print(urllib.urlopen('http://httpbin.org/ip').read())
	print('\n\nAfter proxy:\n')
	print(urllib.urlopen('http://httpbin.org/ip',proxies=proxy).read())


if sys.version_info[0] == 3:
        # for python 3
	import requests
	import urllib.request
	proxy={'http':'http://138.122.2.7:53281'}
	print('without proxy:\n')
	print(urllib.request.urlopen('http://httpbin.org/ip').read())
	print('\n\nAfter proxy:\n')

	from urllib import request as urlrequest
	proxy_host='138.122.2.7:53281'
	url = 'http://www.httpbin.org/ip'
	req = urlrequest.Request(url)
	req.set_proxy(proxy_host, 'http')
	response = urlrequest.urlopen(req)
	print(response.read().decode('utf8'))
	
input()



