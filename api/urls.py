from django.urls import path
from . import views


urlpatterns = [
    path('Events/', views.EventList.as_view(), name="Events"),
    path('Likes/', views.EventLikesList.as_view(), name = "Author"), 
]