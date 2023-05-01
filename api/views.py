from django.http import Http404
from . serializers import *
from . models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status,mixins,generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters



#views to list, create and delete new events
class EventList(APIView):
    def get(self, request, format=None):
        queryset = Events.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request):
        queryset=request.data
        queryset = Events.objects.get(id)
        queryset.delete()
        return Response(queryset.data)
    
class Eventmixin(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
        queryset = Events.objects.all()
        serializer = EventSerializer(queryset, many=True)

        def put(self, request, *args,**kwargs):
            try:
                return self.update(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404
            
        def delete(self, request, *args, **kwargs):
            try:
                return self.destroy(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404
    
class EventListSearch(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['eventDate','eventVenue','eventtitle']
    search_fields = ['^eventSeatingCapacity']

# use the url convention as :
# http://127.0.0.1:8000/evt/Eventsearch/?eventVenue=vile parle
# http://127.0.0.1:8000/evt/Eventsearch/?eventDate=2023-04-30
# http://127.0.0.1:8000/evt/Eventsearch/?search=5



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
    
class Photomixin(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
        queryset = Photo.objects.all()
        serializer = PhotoSerializer(queryset, many=True)

        def put(self, request, *args,**kwargs):
            try:
                return self.update(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404
            
        def delete(self, request, *args, **kwargs):
            try:
                return self.destroy(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404



#views to list, create and delete new event likes
class EventLikesList(APIView):
    def get(self, request, format=None):
        queryset = EventLikes.objects.all()
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data, safe=True)

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
    
class EventLikesmixin(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
        queryset = EventLikes.objects.all()
        serializer = LikeSerializer(queryset, many=True)

        def put(self, request, *args,**kwargs):
            try:
                return self.update(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404
            
        def delete(self, request, *args, **kwargs):
            try:
                return self.destroy(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404
            


#views to list, create and delete new favs
class FavouriteList(APIView):
    def get(self, request, format=None):
        queryset = Favourite.objects.all()
        serializer = FavSerializer(queryset, many=True)

        return Response(serializer.data, safe=True)

    def post(self, request, format=None):
        serializer = FavSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    def delete(self, request):
        queryset=request.data
        queryset = EventLikes.objects.get(id)
        queryset.delete()
        return Response(queryset.data)
    
class Favouritemixin(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
        queryset = Favourite.objects.all()
        serializer = FavSerializer(queryset, many=True)

        def put(self, request, *args,**kwargs):
            try:
                return self.update(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404
            
        def delete(self, request, *args, **kwargs):
            try:
                return self.destroy(request, *args, **kwargs)
            except Events.DoesNotExist:
                raise Http404