from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)


urlpatterns = [
path('user/register/', UserRegistrationAPI.as_view(), name = 'register_user'),
path('committee/register/', UserRegistrationAPI.as_view(), name = 'register_user'),
path('logout/',  TokenBlacklistView.as_view(), name = 'logout_user'),
path('login/', UserLoginView.as_view(), name = 'login_user'),
path('token-refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
path('profile/<str:username>', UserEditView.as_view(), name='user-profile'),
path('profile/faculty/add/<str:username>', FacultyCreateView.as_view(), name='add-faculty'),
path('profile/member/add/<str:username>', MemberCreateView.as_view(), name='add-member'),
]
