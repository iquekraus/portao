from rest_framework import serializers
from .models import EventUsers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUsers
        fields = ('id', 'username', 'password', 'email', 'created')