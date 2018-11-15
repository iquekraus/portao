from rest_framework import serializers
from .models import EventComments
from .models import EventUsers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventComments
        fields = ('id', 'name', 'icon_perfil', 'category', 'comment', 'created')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUsers
        fields = ('id', 'username', 'password', 'email', 'created')