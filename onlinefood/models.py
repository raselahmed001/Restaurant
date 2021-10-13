from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from datetime import date



# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=12, choices=(('USER','USER'),('RESTAURANT','RESTAURANT'),('DRIVER','DRIVER')))
class Socialmedia(models.Model):
    social_name = models.CharField(max_length=10, null=True, blank=True)
    facebook_link = models.CharField(max_length=200, null=True, blank=True)
    twitter_link = models.CharField(max_length=200, null=True, blank=True)
    instagram_link = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.social_name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    social = models.ForeignKey(Socialmedia, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_image = models.FileField(upload_to="images/user_cus/")

    def __str__(self):
        return self.first_name

class Marchent(models.Model):
    owner_name = models.CharField(max_length=100)
    no_of_restaurant = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    social = models.ForeignKey(Socialmedia, on_delete=models.CASCADE)
    mar_image = models.FileField(upload_to="images/mar_image/")
    nid_driving_lic_image = models.FileField(upload_to="images/nid/")
    res_date = models.DateTimeField(auto_now_add=True)
    validation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.owner_name

class Restaurant(models.Model):
    OPEN = 1
    CLOSED = 2

    OPENING_STATUS = (
        (OPEN, 'open'),
        (CLOSED, 'closed'),
        )

    BREAKFAST = 1
    LAUNCH = 2
    DINNER = 3
    DELIVERY = 4
    CAFE = 5
    LUXURY = 6
    NIGHT = 7

    FEATURE_CHOICES = (
        (BREAKFAST, 'breakfast'),
        (LAUNCH, 'launch'),
        (DINNER, 'dinner'),
        (DELIVERY, 'delivery'),
        (CAFE, 'cafe'),
        (LUXURY, 'luxury dining'),
        (NIGHT, 'night life'),
        )

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


    TIMING_CHOICES = (
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday'),
        (SUNDAY, 'sunday'),
        )
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=120, blank=True, null=True)
    restaurant_phone_number = models.PositiveIntegerField()
    url = models.URLField(blank=True, null=True)
    restaurant_email = models.EmailField(blank=True, null=True)
    owner_email = models.EmailField(blank=True, null=True)
    opening_status = models.IntegerField(choices=OPENING_STATUS,default=OPEN)
    email = models.EmailField()
    restaurant_website = models.TextField()
    lit = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    trade_lic_image = models.FileField(upload_to="images/trade_lic/")
    lic_validation_date = models.DateTimeField(null=True, blank=True)
    res_validation_date = models.DateTimeField(null=True, blank=True)
    features = models.IntegerField(choices=FEATURE_CHOICES, default=DINNER)
    timings = models.IntegerField(choices=TIMING_CHOICES, default=MONDAY)
    opening_from = models.TimeField()
    opening_to = models.TimeField()
    social = models.ForeignKey(Socialmedia, on_delete=models.CASCADE)
    other_details = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})

    def averageRating(self):
        reviewCount = self.restaurantreview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.restaurantreview_set.all()])
            return ratingSum / reviewCount


class Category(models.Model):
    name = models.CharField(max_length=120,db_index=True) 
    slug = models.SlugField(max_length=120,db_index=True)
  
    def __str__(self):
        return self.name


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=120,db_index=True)
    slug = models.SlugField(max_length=120,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



class OrderMenu(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."

class DeliveryAgent(models.Model):
    company_name = models.CharField(max_length=510)
    adress = models.TextField()
    mobile1 = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=20)
    manager_name = models.CharField(max_length=50)
    deliver_Charge = models.IntegerField()

    def __str__(self):
        return self.company_name


class  Delivery(models.Model):
    BREAKFAST = 1
    LAUNCH = 2
    DINNER = 3
    DELIVERY = 4
    CAFE = 5
    LUXURY = 6
    NIGHT = 7
    FEATURE_CHOICES = (
        (BREAKFAST, 'breakfast'),
        (LAUNCH, 'launch'),
        (DINNER, 'dinner'),
        (DELIVERY, 'delivery'),
        (CAFE, 'cafe'),
        (LUXURY, 'luxury dining'),
        (NIGHT, 'night life'),
        )

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


    TIMING_CHOICES = (
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday'),
        (SUNDAY, 'sunday'),
        )
    id = models.AutoField(primary_key=True)
    delivery_agent_id = models.ForeignKey(DeliveryAgent, on_delete=models.CASCADE)
    features = models.IntegerField(choices=FEATURE_CHOICES)
    timings = models.IntegerField(choices=TIMING_CHOICES)
    order_quantity = models.PositiveIntegerField(default=1)
    delivery_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class Order_tracking(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    item_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    track_Delivery_agent = models.ForeignKey(DeliveryAgent, on_delete=models.CASCADE)
    
    def __str__(self):
        return "id"

class Rating(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    restaurant_star = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant

class Card(models.Model):
    number = models.CharField(max_length=16)
    expiry = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)

class GPSLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)

