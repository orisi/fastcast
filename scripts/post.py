import requests
url = 'http://54.77.58.8/'

payload = {

            "source": "1",
            "destination": "1",
            "channel": "1",
            "signature": "1",


}


data_x = { "Test" : "test" }

### Create file and open
#import json
#Bwith open('test.json', 'w') as outfile:
#  json.dump(data_x, outfile)

files = {'file': open('test.json', 'rb')}
r = requests.post(url, files=files, data=payload)

print r.text
print r.headers
