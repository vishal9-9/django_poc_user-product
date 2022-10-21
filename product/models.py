from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.response import Response

from user.models import Users

class ProductManager(models.Manager):
    def get_product(self, id):
        try:
            product = Products.objects.get(product_id=id)
            return product
        except Products.DoesNotExist:
            return None

    def update_product(self, id, data):
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        price = data.get('price')
        product_to_update = Products.objects.get(product_id=id)
        if product_to_update:
            if product_name:
                product_to_update.product_name = product_name
            if quantity:
                product_to_update.quantity = quantity
            if price:
                product_to_update.price = price
            product_to_update.save()
            return True
        else:
            raise serializers.ValidationError("No product with that name to update")

    def save_product(self, data, user):
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        price = data.get('price')
        if not Products.objects.filter(product_name=product_name).exists():
            product = {
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'added_by': user,
            }
            Products.objects.create(**product)
            return True
        else:
            raise serializers.ValidationError("Product already registered")

class Products(models.Model):
    # class Meta:
    #     unique_together = (('product_id','product_name'),)

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False, unique=True)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False, default=1)
    added_by = models.ForeignKey(Users, on_delete=models.CASCADE)

    objects = ProductManager()
