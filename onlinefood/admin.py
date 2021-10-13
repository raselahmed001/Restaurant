from django.contrib import admin
from .models import*

@admin.register(Socialmedia)
class SocialmediaAdmin(admin.ModelAdmin):
    list_display = ['facebook_link']
    search_fields = ['facebook_link']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','mobile_number']
    search_fields = ['first_name', 'last_name']

@admin.register(Marchent)
class MarchentAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'no_of_restaurant', 'mobile_number', 'email', 'validation_date']
    search_fields = ['owner_name', 'email', 'mobile_number']
    list_filter = ['res_date', 'validation_date']

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name']
    search_fields = ['restaurant_name', 'email']
    list_filter = ['lic_validation_date', 'res_validation_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['category','name','available']
    search_fields = ['name']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','postal_code']
    search_fields = ['first_name']  

@admin.register(OrderMenu)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order']

@admin.register(DeliveryAgent)
class DeliveryAgentAdmin(admin.ModelAdmin):  
    list_display = ['company_name'] 

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['delivery_agent_id']

@admin.register(Order_tracking)
class Order_trackingAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'item_id']

@admin.register(OrderUpdate)
class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'update_id']


@admin.register(RestaurantReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ['restaurant']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['number']

@admin.register(GPSLocation)
class GPSLocationAdmin(admin.ModelAdmin):
    list_display = ['latitude','longitude']
    

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating','restaurant_star']
