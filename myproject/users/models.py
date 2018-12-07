#from django.db import models
# Create your models here.
from django.db import models
from model_utils.models import TimeStampedModel

class EventUsers(TimeStampedModel):
    username = models.CharField(max_length=25, verbose_name='Username')
    password = models.CharField(max_length=15, verbose_name='Password')
    email = models.CharField(max_length=250, verbose_name='Email')

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Event User'
        verbose_name_plural = 'Event Users'
        #ordering = ['-created']
