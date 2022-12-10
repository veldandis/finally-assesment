# from django.shortcuts import render
# from django.http import JsonResponse
# #from .products import products
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
# from base.models import *
# from base.serializers import *

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# from rest_framework import status

# @api_view(['GET'])
# def getProducts(request):
#     products = Product.objects.all()
#     serailizer = ProductSerializer(products, many=True)
#     return Response(serailizer.data)

# @api_view(['GET'])
# def getProduct(request,pk):
#     product = Product.objects.get(_id=pk)
#     serailizer = ProductSerializer(product, many=False)
#     return Response(serailizer.data)
