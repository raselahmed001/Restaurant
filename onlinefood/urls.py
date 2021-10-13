from django.conf.urls import  url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.UserList.as_view(),name='user'),
   path('Category/', views.CategoryList.as_view(), name='Category-list'),
   path('Socialmedia/', views.SocialmediaList.as_view(), name='Socialmedia-list'),
   path('Marchent/', views.MarchentList.as_view(), name='Marchent-list'),
   path("Restaurant/<int:pk/", views.RestaurantList.as_view, name="Restaurant"),
   path('Menu/', views.MenuList.as_view(), name='Menu-list'),
   path('Order/', views.Orderlist.as_view(), name='Order-list'),
   path('OrderMenu/', views.OrderMenuList.as_view(), name='OrderMenu-list'),
   path('OrderUpdate/', views.OrderUpdateList.as_view(), name='OrderUpdate-list'),
   path('Review/', views.RestaurantReviewList.as_view(), name='Review-list'),
   path('DeliveryAgent/', views.DeliveryAgentList.as_view(), name='DeliveryAgent-list'),
   path('Delivery/', views.DeliveryList.as_view(), name='Delivery-list'),
   path('Order_tracking/', views.Order_trackingList.as_view(), name='Order_tracking-list'),
   path('Card/', views.CardList.as_view(), name='Card-list'),
   path('GPSLocation/', views.GPSLocationList.as_view(), name='GPSLocation-list'),
   path('Rating/', views.RatingList.as_view(), name='Rating-list'),

   
    
]
