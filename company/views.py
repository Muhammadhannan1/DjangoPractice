from django.shortcuts import render
from rest_framework import viewsets
from company.models import Products
from company.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# class ProductViewSet(viewsets.ModelViewSet):
#         queryset = Products.objects.all()
#         serializer_class = ProductSerializer


@api_view(['GET'])
def getProduct(request):
    product_obj = Products.objects.all()
    serializer = ProductSerializer(product_obj,many = True) 

    return Response({'success':True,'status': 200, 'data': serializer.data})


@api_view(['POST'])
def addProduct(request):
    data = request.data
    serializer = ProductSerializer(data=request.data)

    if not serializer.is_valid():
        
        return Response({'status':404,'message':serializer.errors})
    serializer.save()
    return Response({'status':200,'message':'Product created successfully','success':True,'data':serializer.data})