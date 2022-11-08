from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserRegistrationView.as_view(), name='user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('car/', CarView.as_view(), name='car'),
    path('car/<int:pk>/', CarView.as_view(), name='car_pk'),
    path('ad/', AdView.as_view(), name='ad'),
    path('ad/<int:pk>/', AdView.as_view(), name='ad_pk'),
]