from django.db import models

# Create your models here.
class Msg( models.Model ):
    """
    Model for storing `messages`
    """

    message_id = models.CharField( max_length = 100 )
    timestamp = models.DateTimeField()
    source = models.CharField( max_length = 100 )
    destination = models.CharField( max_length = 100 )
    channel = models.CharField( max_length = 100 )
    signature = models.CharField( max_length = 100 )
    body = models.BinaryField()

