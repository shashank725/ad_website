from rest_framework import serializers

from django.contrib.auth.models import User
from .models import UserProfile, Car, Ad

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        
        # UserProfile.objects.create(user=user)
        user_profile = UserProfile(user=user)
        user_profile.save()
        
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['user', 'car_id', 'car_model', 'car_brand', 'number_plate']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['user', 'ad_id', 'ad_title', 'ad_description', 'ad_price', 'ad_image']