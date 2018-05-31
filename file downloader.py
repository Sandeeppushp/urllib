import sys

link='https://www.python.org/static/img/python-logo@2x.png'
filename='file.jpg'

if sys.version_info[0] < 3:
        #for python 2
        import urllib
        download=urllib.urlretrieve(link,filename)
        print(download)


if sys.version_info[0] == 3:
        #for python 3
        import urllib.request
        download=urllib.request.urlretrieve('https://www.python.org/static/img/python-logo@2x.png','a.jpg')
        print(download)

input()
