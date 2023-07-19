from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = [i['image'] for i in ImageSerializer(EventsImage.objects.filter(image_fk = data['id']),many=True).data]
        return data

class ImageSerializer(serializers.ModelSerializer):
     class Meta:
        model = EventsImage
        fields = ["image"]
        depth = 0

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLikes
        fields = '__all__'

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'