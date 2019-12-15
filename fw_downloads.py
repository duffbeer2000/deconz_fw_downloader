#!/usr/bin/env python
"""
Snipped to download current IKEA ZLL OTA files into ~/otau
compatible with python 3.
"""

import os, json, requests, re, time
try:
	from urllib.request import urlopen, urlretrieve
except ImportError:
	from urllib2 import urlopen
	from urllib import urlretrieve


f = urlopen("http://fw.ota.homesmart.ikea.net/feed/version_info.json")
data = f.read()

arr = json.loads(data)
"""
otapath = '%s/otau' % os.path.expanduser('~')
"""
otapath = '/otau'

if not os.path.exists(otapath):
	os.makedirs(otapath)

for i in arr:
	if 'fw_binary_url' in i:
		url = i['fw_binary_url']
		ls = url.split('/')
		fname = ls[len(ls) - 1]
		path = '%s/%s' % (otapath, fname)

		if not os.path.isfile(path):
			urlretrieve(url, path)
			print(path)
		else:
		    print('%s already exists' % fname)


"""
Snipped to download current OSRAM OTA files into ~/otau
compatible with python 3.
"""

response = requests.get("https://api.update.ledvance.com/v1/zigbee/products")
response = json.loads(response.content)

productlist = response['products']
for x in range(len(productlist)):
    time.sleep(35)
    company = productlist[x].get('id').get('company')
    product = productlist[x].get('id').get('product')
    url = 'https://api.update.ledvance.com/v1/zigbee/firmwares/download/%s/%s/latest' % (company, product)
    response = requests.get(url)
    firmwarecontent = response.content
    fname = response.headers['Content-Disposition']
    fname = re.findall("filename=(.+)", fname)[0]
    fname = fname.split(";")
    fname = fname[0]
    
    path = '%s/%s' % (otapath, fname)
	
    if not os.path.isfile(path):
        file = open(path, "wb")
        file.write(firmwarecontent)
        file.close()
        print(path)
    else:
        print('%s already exists' % fname)
