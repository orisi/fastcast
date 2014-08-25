from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UnixEpochDateField(serializers.DateTimeField):
    def to_native(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def from_native(self, value):
        import datetime
        return datetime.datetime.fromtimestamp(int(value))
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

from msg.models import Msg

class MsgSerializer( serializers.ModelSerializer ):
    epoch = UnixEpochDateField(source='timestamp')
        
    class Meta:
        model = Msg
        fields = ('frame_id','timestamp','source','channel','signature','body','epoch')
 
