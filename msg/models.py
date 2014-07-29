from django.db import models

# Create your models here.
class Msg( models.Model ):
    """
    Model for storing `messages`
    """
   
    subject = models.CharField( max_length = 100 )
    origin = models.CharField( max_length = 100 )
    channel = models.CharField( max_length = 100 )
    message_id = models.CharField( max_length = 100 )
    pubkey_list = models.CharField( max_length = 100 )
    miners_fee_satoshi = models.CharField( max_length = 100 )
    prevtxs = models.CharField( max_length = 100 )
    outputs = models.CharField( max_length = 100 )
    req_sigs = models.CharField( max_length = 100 )
    operation = models.CharField( max_length = 100 )
    sum_satoshi = models.CharField( max_length = 100 )
    locktime = models.CharField( max_length = 100 )

