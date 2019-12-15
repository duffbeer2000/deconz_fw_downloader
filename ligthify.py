import requests
import json
import re
import time
import os

otapath = '/otau'

if not os.path.exists(otapath):
	os.makedirs(otapath)

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