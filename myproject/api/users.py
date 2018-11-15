from django.shortcuts import render
from rest_framework.views import APIView
from .models import EventUsers
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class UserListView(APIView):

    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        users = EventUsers.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
