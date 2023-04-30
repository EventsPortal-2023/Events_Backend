from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
     
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLikes
        fields = '__all__'

