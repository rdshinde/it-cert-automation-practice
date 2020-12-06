
import json
import urllib.request
from urllib.parse import*
import ssl

# Ignore SSL certificate errors

import json
import urllib

#Stroring the given parameters
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
sample_address = input("Enter location: ")
url = serviceurl + urllib.parse.urlencode({'address': sample_address , 'key':42})
print('retrieving',url)


#Obtaining and reading the data
data = urllib.request.urlopen(url).read()
print('Retrieved',len(data),'characters')
#Parsing the data and looking for the field we want.
#That field is inside the "Results" array, in its first item (if our address is
#correct we can assume that the result would be the correct one) and on its
#"place_id" field
jsondata = json.loads(data)
print(json.dumps(jsondata,indent = 4))
print("PLACE ID: ", jsondata['results'][0]['place_id'])
