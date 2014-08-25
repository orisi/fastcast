from django.db import models
from django.core.exceptions import ValidationError

import uuid # from http://zesty.ca/python/uuid.html
import sys
import base64 


def to_native(value):
    """ Return epoch time for a datetime object or ``None``"""
    import time
    try:
       return int(time.mktime(value.timetuple()))
    except (AttributeError, TypeError):
       return None


        
 
def fetch_code(custom_string="CODE_"):
    """
    usage:
    fetch_code()   
    fetch_code(custom_string="KEY_")
  
    """
    b64uid = '00000000'
    
   
    uid = uuid.uuid4()
    b64uid = base64.b64encode(uid.bytes,'-_')
    
    code = b64uid[0:6]
    return custom_string+code

# Create your models here.
class Msg( models.Model ):
    """
    Model for storing `messages`
    """

    def validate_file(fieldfile_obj):
        """
        Validation of size
        """
        filesize = fieldfile_obj.file.size
        kilobyte_limit = 65
        if filesize > kilobyte_limit*1024:
            raise ValidationError("Max file size is %skB" % str(kilobyte_limit))

    frame_id = models.CharField( max_length = 255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField( max_length = 255 )
    channel = models.CharField( max_length = 255 )
    signature = models.CharField( max_length = 255 )
    #body = models.FileField(upload_to="messages/%Y/%m/%d/", validators=[validate_file],blank=True)

    body = models.TextField(blank=True)
    epoch = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        self.frame_id = fetch_code(custom_string="0_")
        self.epoch = to_native(self.timestamp)
        super(Msg, self).save(*args, **kwargs)

