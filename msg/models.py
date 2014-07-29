from django.db import models
from django.core.exceptions import ValidationError

import uuid # from http://zesty.ca/python/uuid.html
import sys
import base64 
 
 
def fetch_code(custom_string="CODE_'):
    """
    takes an optional argument, a string to be put at the beginning of a code,
    so the code will look like that:
 
    CODE_8mANDJ
    KEY_9coOeC
 
    default is CODE_
 
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

    message_id = models.CharField( max_length = 100 )
    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField( max_length = 100 )
    destination = models.CharField( max_length = 100 )
    channel = models.CharField( max_length = 100 )
    signature = models.CharField( max_length = 100 )
    body = models.FileField(upload_to="messages/%Y/%m/%d/", validators=[validate_file])


