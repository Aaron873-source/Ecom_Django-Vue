from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

#Going to simply use APIView Methods built inside the Django rest framework going to help us with HTTP API method calls
# 

class LatestProductsList(APIView):

# NOTE : When Inheriting from the APIView class it has pre-built methods for HTTP METHOD LIKE GET , POST, for the desired case we just want to override the method for our need like below for products

    def get(self, request, format=None):

        #quering all products from the database
        products = Product.objects.all()[0:4]

        #Convert the products to JSON to be diplayed in the front end using the serializer
        serializer = ProductSerializer(products, many=True)

        #Now after serializing/ converting the Object model to JSON we return it as the response
        return Response(serializer.data)

