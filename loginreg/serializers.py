from .models import User,UserProfile,Faculty,Member
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=180)
    password = serializers.CharField(max_length=180)

    def validate(self, attrs):
        username = attrs.get('username')
        user = User.objects.filter(username=username)
        if user:
            return attrs
        else:
            msg={
                'detail': 'User does not exists.', 'register': True}
            raise serializers.ValidationError(msg, code='authorization')

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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('bio')

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'faculty_name')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'member')

