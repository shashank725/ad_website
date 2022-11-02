from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField(max_length=500, blank=True)
    # city = models.CharField(max_length=50, blank=True)
    # state = models.CharField(max_length=50, blank=True)
    # country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username, self.user.first_name

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.IntegerField(primary_key=True)
    car_model = models.CharField(max_length=50)
    car_brand = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=100)

    def __str__(self):
        return self.car_id, self.car_model

class Ads(models.Model):
    user = models.ManyToManyField(User)
    ad_id = models.IntegerField(primary_key=True)
    ad_title = models.CharField(max_length=50)
    ad_description = models.TextField(max_length=500)
    ad_price = models.IntegerField()

    def __str__(self):
        return self.ad_id, self.ad_title, self.ad_price

