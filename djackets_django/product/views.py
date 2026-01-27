from django.http import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response, Serializer

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


#Creating a new viewset class to handle returning the details of objects
class ProductDetail(APIView):

    #HAVING INHERITED FROM THE API VIEW WE ARE NOT GOING TO OVERIDE THE GET FUNCTION BUT INSTEAD OVERRIDE THE GET OBJECT FUNCTION AND PASS IN 
    def get_object(self, category_slug,product_slug):
        try:
            return Product.objects.filter(category_slug = category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    #NOW OVERRIDE THE GET FUNCTION TO USE THE ABOVE OVERRIDEN get_object function
    def get(self, request, category_slug, product_slug,format=None):
        product = self.get_object(category_slug, product_slug)
        #Still want to use the serializer to convert the object to JSON ofcourse
        serializer = ProductSerializer(product)

        #Return the JSON
        return Response(serializer.data)

