from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from uuid import uuid4
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework import status

# Create your views here

class UserRegistrationAPI(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':422, 'errors': serializer.errors, 'message': 'Unprocessable Entity'})

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({'status': 200, 'payload' : {"User username" : user.username , "User id" : user.id},'message' : 'Registration Successful', 'refresh': str(refresh), 'access': str(refresh.access_token)})
    
class UserLoginView(APIView):
    # permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)