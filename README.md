```
echo test > test.json

curl -X POST -S -H 'Accept: application/json' /
-F "message_id=s12332432" /
-F "source=s12332432" /
-F "destination=s12332432" /
-F "channel=s12332432" /
-F "signature=signature" /
-F "body=@test.json;type=image/jpg" 127.0.0.1:8000/last?format=json
```
