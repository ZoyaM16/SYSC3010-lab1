import httplib
import urllib
import time
key = "AT68QYQ94MQEWXL3"  # Put your API Key here
ProjGroup=('L3-T-3a');
cmail=('zoya.mushtaq@carleton.ca');
identifier=('a');
params = urllib.urlencode({'field1': ProjGroup, 'field2':cmail, 'field3': identifier, 'key':key })
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
try:
            conn.request("POST", "/update",params,headers)
            response = conn.getresponse()
            print response.status, response.reason
            data = response.read()
            conn.close()
except:
            print "connection failed"

