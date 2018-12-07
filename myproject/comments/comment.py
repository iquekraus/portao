from django.shortcuts import render
from rest_framework.views import APIView
from .models import EventComments
from .serializer import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class CommentView(APIView):

    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = CommentSerializer

    def get(self, request, pk):
        comment = EventComments.objects.get(pk=pk)
        serializer = self.serializer_class(comment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        comment = EventComments.objects.get(pk=pk)
        serializer = self.serializer_class(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            comment = EventComments.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)