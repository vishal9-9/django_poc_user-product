import json
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Products
from product.serializers import ProductCreationSerializer, ProductUpdatingSerializer

# Create your views here.

class ProductCreationView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        products_list = Products.objects.all()
        if products_list:
            to_return = []
            for product in products_list:
                serialized_data = ProductCreationSerializer(product)
                to_return.append(serialized_data.data)
            return Response({"status": 200, "success_message": to_return},status=200)
        return Response({"status": 404, "error_message": ""},status=404)

    def post(self, request):
        serialized_data = ProductCreationSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            if Products.objects.save_product(serialized_data.data, request.user):
                return Response({"status": 200, "success_message": f'Product added {serialized_data.data}'},status=200)
        return Response({"status": 400, "error_message": "Failed"},status=400)

class ProductUpdatingView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, id):
        try:
            to_return = Products.objects.get_product(id=id)
            if to_return != None:
                serializer = ProductUpdatingSerializer(to_return)
                to_return = serializer.data
                return Response({"status": 200, "success_message": to_return},status=200)
            else:
                return Response({"status": 404, "error_message": "No product with that id"},status=404)
        except Exception as e:
            raise e

    def post(self, request, id):
        serialized_data = ProductUpdatingSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            if Products.objects.update_product(id, serialized_data.data):
                return Response({"status": 200, "success_message": f'Product updated {serialized_data.data}'},status=200)
        return Response({"status": 400, "error_message": "Unable to update product"},status=400)
