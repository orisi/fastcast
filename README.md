# FASTCAST

FastCast is a simple broadcast messaging protocol we had to develop for [Orisi](http://orisi.org). Right now it supports a single-server hub, but it should be possible to [extend it into a distributed architecture](https://github.com/orisi/fastcast/issues/1), and to include a [proof-of-work](https://en.bitcoin.it/wiki/Proof_of_work) or [proof-of-burn](https://en.bitcoin.it/wiki/Proof_of_burn) spam prevention.

FastCast is built as a simple web REST server based on Django Rest Framework. Here you can read [how it compares to BitMessage](https://github.com/orisi/fastcast/wiki/How-FastCast-compares-to-BitMessage).

You can explore API following e.g. those urls:
* [Messages from the last 10 minutes](http://hub.orisi.org/last)
* [Last 10 messages](http://hub.orisi.org?page_size=10)

The default FASTCAST server is  [hub.orisi.org](http://hub.orisi.org).
You can install your own using this repo if you like.

# Implementations

## Bash

### Posting new message
```
echo test > test.json

curl -X POST -S -H 'Accept: application/json' /  -F "source=s12332432" / -F "destination=s12332432" -F "channel=s12332432" -F "signature=signature" -F "body" 127.0.0.1:8000/last/
```

### Getting messages from last 10 minutes

```
curl -X GET http://hub.orisi.org/last/?format=json
```



## Python

### Posting new message



```
import requests
url = 'http://54.77.58.8/'

payload = {

            "source": "1",
            "destination": "1",
            "channel": "1",
            "signature": "1",
            "body": "1",


}



r = requests.post(url, data=payload)

print r.text
```

### Get messages from last 10 minutes

```
import requests
url = 'http://hub.orisi.org/last?format=json'
r = requests.get(url)
```

### Get body

```
import requests

...

url = 'http://hub.orisi.org/storage' + message.body
r = requests.get(url)
```







