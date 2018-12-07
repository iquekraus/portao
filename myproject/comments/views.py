from django.shortcuts import render
from rest_framework.views import APIView
from .models import EventComments
from .serializer import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class CommentListView(APIView):

    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = CommentSerializer

    def get(self, request, format=None):
        comments = EventComments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
