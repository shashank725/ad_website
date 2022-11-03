from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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

        # if serializer.is_valid(raise_exception=True):
        if serializer.is_valid():
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
        serializer = CarSerializer(data=request.data, context={"user":request.user})
        if serializer.is_valid(raise_exception=True):
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
            ad = get_object_or_404(Ad, pk=pk)
            serializer = AdSerializer(ad)
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

# @csrf_exempt
# class UserLoginView(APIView):
#     def post(self, request, format=None):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data.get('email')
#         password = serializer.data.get('password')
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             token = get_tokens_for_user(user)
#             return Response({'token':token, 'message':'Login Success'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'errors':{'non_field_errors':['Email or Password is not valid']}}, status=status.HTTP_400_BAD_REQUEST)
