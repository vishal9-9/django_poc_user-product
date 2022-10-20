from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Products
from product.serializers import ProductCreationSerializer, ProductUpdatingSerializer

# Create your views here.

class ProductCreationView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serialized_data = ProductCreationSerializer(data=request.data, context={'user': request.user})
        if serialized_data.is_valid(raise_exception=True):
            return Response({"status": 200, "success_message": f'Product added {serialized_data.data}'},status=200)
        return Response({"status": 400, "error_message": "Failed"},status=400)

class ProductUpdatingView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serialized_data = ProductUpdatingSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            if Products.objects.update_product(serialized_data.data):
                return Response({"status": 200, "success_message": f'Product updated {serialized_data.data}'},status=200)
        return Response({"status": 400, "error_message": "Unable to update product"},status=400)
