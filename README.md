# FASTCAST

Fast cast is a simple web REST server based on Django Rest Framework. It handles internal messaging services for Orisi nodes. It is robust and easy to distribute.

You can explore API following those urls:
* [Messages from last 10 minutes](http://hub.orisi.org/last)
* [Last 10 messages](http://hub.orisi.org?page_size=10)


# Implementations

## Bash

### Posting new message
```
echo test > test.json

curl -X POST -S -H 'Accept: application/json' /  -F "source=s12332432" / -F "destination=s12332432" -F "channel=s12332432" -F "signature=signature" -F "body=@test.json;type=image/jpg" 127.0.0.1:8000/last/
```

### Getting messages from last 10 minutes

```
curl -X GET http://hub.orisi.org/last/?format=json
```

### Getting message body

```
curl -X GET http://hub.orisi.org/storage/messages/2014/07/29/test_3.json
```

## Python

### Posting new message



```
import requests
url = 'http://hub.orisi.org/'

payload = {

            "source": "1",
            "destination": "1",
            "channel": "1",
            "signature": "1",


}


### Create file and open


files = {'file': open('test.json', 'rb')}
r = requests.post(url, files=files, data=payload)



```

### Get messages from last 10 minutes

```
import requests
url = 'http://hub.orisi.org/last?format=json'
r = requests.get(url)
```


## Technical Notes

Messages have headers

And body. Up to 65 kbytes json file.
Files are sharded on day-basis.



