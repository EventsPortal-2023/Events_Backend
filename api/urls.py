from django.urls import path
from . import views


urlpatterns = [

    path('Events/', views.EventList.as_view(), name="Events"),
    path('Events/<int:pk>', views.Eventmixin.as_view(), name="Events"),

    path('Eventsearch/', views.EventListSearch.as_view(), name="Events"),

    path('photos/', views.PhotoList.as_view(), name="Events"),
    path('photos/<int:pk>', views.Photomixin.as_view(), name="Events"),

    path('Likes/', views.EventLikesList.as_view(), name = "Likes"),
    path('Likes/<int:pk>', views.EventLikesmixin.as_view(), name="Likes"),


    path('favs/',  views.FavouriteList.as_view(), name="Favourite"),
    path('favs/<int:pk>',  views.Favouritemixin.as_view(), name="Favourite"),
]