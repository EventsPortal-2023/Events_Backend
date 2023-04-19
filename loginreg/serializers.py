from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if data.get('sapid') is not None:
            sapid = data.get('sapid')
            if sapid and (not sapid.isdigit()):
                raise serializers.ValidationError({'error': 'Sapid must contain only digits.'})
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create( 
            username = validated_data.get('username'),
            sapid=validated_data.get('sapid',None),
            committee=validated_data.get('committee',None),
            college=validated_data.get('college',None),
            is_user=validated_data.get('is_user', False),
            is_committee=validated_data.get('is_committee', False)
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)