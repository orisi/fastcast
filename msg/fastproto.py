import json
import requests

headers = {'content-type': 'application/json'}


def constructMessage():
    """
    Message_id, and Timestamp are given by server
    """

    # request = kwargs

    request  = {"message_id": "0_BGG0si", "timestamp": "2014-07-31T14:38:49.541Z", "source": "1", "destination": "1", "channel": "1", "signature": "1", "body": "1"}

    payload = json.dumps(request)

    # signature should be body confirmed

    return payload


def sendMessage(payload):
    url = 'http://54.77.58.8?format=json'
    r = requests.post(url, data=payload, headers=headers)
    print r.text
    return r.text


def getMessages():
    url = 'http://54.77.58.8?format=json'
    r = requests.get(url)
    print r.text
    return r.json


#getMessages()

sendMessage(constructMessage())