from django.urls import path
from . import views


urlpatterns = [
    path('Events/', views.EventList.as_view(), name="Events"),
<<<<<<< HEAD
    path('Likes/', views.EventLikesList.as_view(), name = "Author"), 
=======
    path('Events/<int:pk>', views.Eventmixin.as_view(), name="Events"),
    path('Eventsearch/', views.EventListSearch.as_view(), name="Events"),
    path('Likes/', views.EventLikesList.as_view(), name = "Author"),
    path('photos/<int:pk>', views.Photomixin.as_view(), name="Events"),
    path('Likes/<int:pk>', views.EventLikesmixin.as_view(), name="Author"),
>>>>>>> d76482f749f2574f81e72fefd0ecc8be4c60e293
]