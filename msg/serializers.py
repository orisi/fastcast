from django.contrib.auth.models import User, Group
from rest_framework import serializers

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

import base64
import binascii

def verify(message, signature_b64, pub_b64):
  pub = base64.decodestring(pub_b64)
  signature = base64.decodestring(signature_b64)
  key = RSA.importKey(pub)
  signer = PKCS1_v1_5.new(key)
  digest = SHA256.new()
  digest.update(message)
  if signer.verify(digest, signature):
    return True
  return False

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

from msg.models import Msg, Ping
from datetime import datetime

class MsgSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Msg
        fields = ('frame_id','timestamp','source','channel','signature','body','epoch')
        read_only_fields = ('epoch',)

    def validate(self, attrs):
      try:
        body = base64.decodestring(attrs['body'])
      except binascii.Error:
        raise serializers.ValidationError("Body must be base64 encoded string")

      try:
        verified = verify(body, attrs['signature'], attrs['source'])
        Ping.objects.create(attrs['source'],datetime.utcnow())
      except binascii.Error:
        verified = False

      if not verified:
        raise serializers.ValidationError("The message is not signed by proper signature")

      return attrs
