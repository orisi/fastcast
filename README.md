# Bash

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



# Python

### Posting new message

```
url = 'http://hub.orisi.org/'

payload = {'key1': 'value1', 'key2': 'value2'}


# Create file and open


files = {'file': open('test.json', 'rb')}
r = requests.post(url, files=files, data=payload)



```




