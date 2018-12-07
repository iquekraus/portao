#from django.db import models
# Create your models here.
from django.db import models
from model_utils.models import TimeStampedModel
class EventComments(TimeStampedModel):
    name = models.CharField(max_length=25, verbose_name='Name')
    icon_perfil = models.CharField(max_length=100, verbose_name='Icon_Perfil')
    category = models.CharField(max_length=15, verbose_name='Category')
    comment = models.CharField(max_length=250, verbose_name='Comment')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Event Coment'
        verbose_name_plural = 'Event Coments'
        #ordering = ['-created']
