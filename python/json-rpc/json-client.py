#!/usr/bin/python

import urllib
import json


# retrieve listing
url = 'http://localhost:8888/api/v1/listrecord'
print "retriving data from url: ", url

u = urllib.urlopen(url)

s=u.read()

if len(s)>0:
   # retrieve elements.
   listing=json.loads(s)
   for identifier in listing:
       url = 'http://localhost:8888/api/v1/getrecord/%s' %(identifier)
       u = urllib.urlopen(url)
       print u.read()

else: 
   print "data not returned"

