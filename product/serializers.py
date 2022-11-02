from rest_framework import serializers

from product.models import Products

class ProductCreationSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()
    price = serializers.FloatField()

    class Meta:
        model=Products
        fields=['product_name','quantity','price']

class ProductUpdatingSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(required=False)
    price = serializers.FloatField(required=False)

    class Meta:
        model=Products
        fields=['product_name' ,'price' , 'quantity']
