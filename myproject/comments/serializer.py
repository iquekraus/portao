from rest_framework import serializers
from .models import EventComments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventComments
        fields = ('id', 'name', 'icon_perfil', 'category', 'comment', 'created')
