import requests
#import json
#from requests_toolbelt import MultipartEncoder
# https://github.com/alankbi/detecto/blob/master/docs/index.rst

addr = 'http://localhost:5000'
url = addr + '/ufo'

lena = 'testImages\Lenna.png'
plane = 'trainimages\30.jpg'

files = {
	'name': (None, 'plane'),
	'mail': (None, 'jj@gmail.com'),
    'about': (None, 'plane detector'),
	'file': open('trainimages\\30.jpg', 'rb')
	}
requests.post(url, files=files)

# m = MultipartEncoder(
    # fields={"name":"lena", "class":"girl",
            # 'file': ('filename', open('testImages\Lenna.png', 'rb'))}
    # )
# r = requests.post(url, data=m)
#print (r.text)