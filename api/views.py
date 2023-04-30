from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import status


#views to list, create and delete new events
class EventList(APIView):
    def get(self, request, format=None):
        queryset = Events.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data, safe=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request):
        queryset=request.data
        queryset = Events.objects.get(id)
        queryset.delete()
        return Response(queryset.data)


#views to list, create and delete new photos
class PhotoList(APIView):
    def get(self, request, format=None):
        queryset = Photo.objects.all()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    def delete(self, request):
        queryset=request.data
        queryset = Photo.objects.get(id)
        queryset.delete()
        return Response(queryset.data)
    
#views to list, create and delete new event likes
class EventLikesList(APIView):
    def get(self, request, format=None):
        queryset = EventLikes.objects.all()
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    def delete(self, request):
        queryset=request.data
        queryset = EventLikes.objects.get(id)
        queryset.delete()
        return Response(queryset.data)