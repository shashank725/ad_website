from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Generate Token Manually
from rest_framework_simplejwt.tokens import RefreshToken
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.

class UserRegistrationView(APIView):
    # renderer_classes = [UserRenderers]
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
        # if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = get_tokens_for_user(user)
        
        # serializer = UserProfileSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(user=user)

            return Response({'success': True, 'token':token}, status=status.HTTP_201_CREATED)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)


class CarView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        # cars = Car.objects.all(request.user)
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)

class AdView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            ads = Ad.objects.all(id=pk)
            serializer = AdSerializer(ads, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        ad = Ad.objects.get(id=pk)
        serializer = AdSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None, format=None):
        ad = Ad.objects.get(id=pk)
        ad.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)