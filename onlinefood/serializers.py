from django.urls import path, include
from rest_framework import serializers 
from django.contrib.auth.models import User
from onlinefood.models import *
from random import randint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url','username', 'password', 'first_name')
       

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name',)


class SocialmediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Socialmedia
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = "__all__"

class MarchentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Marchent
        fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields =  "__all__"
        

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"

class OrderMenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderMenu
        fields = "__all__"

class OrderUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderUpdate
        fields = "__all__"


class DeliveryAgentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeliveryAgent
        fields = "__all__"

class DeliverySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Delivery
        fields = "__all__"

class Order_trackingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order_tracking
        fields = "__all__"

class RestaurantReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RestaurantReview
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields =  "__all__"

class GPSLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSLocation
        fields =  "__all__"


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id','restaurant_star', 'order', 'restaurant', 'user')

    