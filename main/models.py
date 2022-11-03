from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    no = models.AutoField(primary_key=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.no

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    # city = models.CharField(max_length=50, blank=True)
    # state = models.CharField(max_length=50, blank=True)
    # country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.IntegerField(primary_key=True)
    car_model = models.CharField(max_length=50)
    car_brand = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=100)

    def __str__(self):
        return self.car_id, self.car_model

class Ad(models.Model):
    user = models.ManyToManyField(User)
    a_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price_per_km = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    ad_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.a_id, self.title, self.price_per_km

class UserAd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username, self.ad.title