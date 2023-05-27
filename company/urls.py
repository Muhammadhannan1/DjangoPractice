


from django.contrib import admin
from django.urls import path,include
from company.views import *
#from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('products/get/', getProduct),
    path('products/create/', addProduct),
]
