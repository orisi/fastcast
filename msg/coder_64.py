import base64

def decode_data(data):
        return base64.decodestring(data)

def code_data(data):
        base64.encodestring(data)
