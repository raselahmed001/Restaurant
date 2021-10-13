from django.shortcuts import render
from .serializers import *
from .models import*
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class SocialmediaList(generics.ListCreateAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialmediaSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = SocialmediaSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)


class MarchentList(generics.ListCreateAPIView):
    queryset = Marchent.objects.all()
    serializer_class = MarchentSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = MarchentSerializer(queryset, many=True)
        return Response(serializer.data)

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)


class Orderlist(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderMenuList(generics.ListCreateAPIView):
    queryset = OrderMenu.objects.all()
    serializer_class = OrderMenuSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = OrderMenuSerializer(queryset, many=True)
        return Response(serializer.data)

class OrderUpdateList(generics.ListCreateAPIView):
    queryset = OrderUpdate.objects.all()
    serializer_class = OrderUpdateSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = OrderUpdateSerializer(queryset, many=True)
        return Response(serializer.data)

class DeliveryAgentList(generics.ListCreateAPIView):
    queryset = DeliveryAgent.objects.all()
    serializer_class = DeliveryAgentSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = DeliveryAgentSerializer(queryset, many=True)
        return Response(serializer.data)


class DeliveryList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = DeliverySerializer(queryset, many=True)
        return Response(serializer.data)


class Order_trackingList(generics.ListCreateAPIView):
    queryset = Order_tracking.objects.all()
    serializer_class = Order_trackingSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = Order_trackingSerializer(queryset, many=True)
        return Response(serializer.data)

class RestaurantReviewList(generics.ListCreateAPIView):
    queryset = RestaurantReview.objects.all()
    serializer_class = RestaurantReviewSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = RestaurantReviewSerializer(queryset, many=True)
        return Response(serializer.data)



class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminUser]
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)


class GPSLocationList(generics.ListCreateAPIView):
    queryset = GPSLocation.objects.all()
    serializer_class = GPSLocationSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = GPSLocationSerializer(queryset, many=True)
        return Response(serializer.data)

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    

    def get(self, request):
        queryset = self.get_queryset()
        serializer = RatingSerializer(queryset, many=True)
        return Response(serializer.data)