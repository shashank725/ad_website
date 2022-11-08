from rest_framework import serializers

from django.contrib.auth.models import User
from .models import UserProfile, Car, Ad, Address


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'user_profile', 'address']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        # UserProfile.objects.create(user=user)
        # user_profile = UserProfile(user=user)
        # user_profile.save()
        
        user_profile_data = validated_data.pop('user_profile')
        address_data = validated_data.pop('address')
        user = User.objects.create_user(**validated_data)
        address = Address.objects.create(**address_data)
        UserProfile.objects.create(user=user, address=address, **user_profile_data)

        return user


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
    def create(self, validated_data):
        # user = self.context['request'].user
        user = self.context.get("request")
        print("USER = ", user)
        car = Car.objects.create(user=user, **validated_data)
        return car


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class AdDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    vehicle_brand_and_model = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return f"{obj.user.f_name} {obj.user.l_name}"

    def get_vehicle_brand_and_model(self, obj): 
        return f""

    class Meta:
        model = Ad
        fields = [
            'user_name', 'ad_id', 'title', 
            'description', 'ad_price', 'ad_image',
            'date_created'
        ]