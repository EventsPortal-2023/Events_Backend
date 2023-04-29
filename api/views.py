from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

class EventList(APIView):
    def get(self, request, format=None):
        snippets = Events.objects.all()
        serializer = EventSerializer(snippets, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data, safe=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoList(APIView):
    def get(self, request, format=None):
        snippets = Photo.objects.all()
        serializer = PhotoSerializer(snippets, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
class EventLikesList(APIView):
    def get(self, request, format=None):
        snippets = EventLikes.objects.all()
        serializer = LikeSerializer(snippets, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
