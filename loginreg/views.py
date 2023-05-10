from rest_framework.generics import GenericAPIView
from .models import User,Faculty,Member
from .serializers import UserSerializer,MemberSerializer,FacultySerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import status,generics
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

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
    
class UserLoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserEditView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        username = self.kwargs.get('username')
        user = self.queryset.filter(username=username).first()
        if not user:
            return Response({'status': 404, 'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        return user

class FacultyCreateView(generics.CreateAPIView):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()

    def post(self, request, username):
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'status': 404, 'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        faculty = Faculty(user=user, faculty_name=serializer.validated_data['faculty_name'])
        faculty.save()

        return Response({'status': 201, 'payload': serializer.data, 'message': 'Faculty member added successfully.'}, status=status.HTTP_201_CREATED)


class MemberCreateView(generics.CreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def post(self, request, username):
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'status': 404, 'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        member = Member(user=user, member=serializer.validated_data['member'])
        member.save()

        return Response({'status': 201, 'payload': serializer.data, 'message': 'Committee member added successfully.'}, status=status.HTTP_201_CREATED)