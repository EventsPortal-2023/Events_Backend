from rest_framework import serializers
from django.contrib.auth.models import User
<<<<<<< HEAD
from models import *
=======
from .models import *
>>>>>>> d76482f749f2574f81e72fefd0ecc8be4c60e293

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

