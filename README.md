echo test > test.json

curl -X POST -H "Content-Type:multipart/form-data" -F "body=@test.json;type=image/jpeg" http://hub.orisi.org -F {

 "message_id": "", 
 "source": "", 
 "destination": "", 
 "channel": "", 
 "signature": "", 
    }
