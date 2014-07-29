from django.db import models
from django.core.exceptions import ValidationError
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

