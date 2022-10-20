from django.db import models

from user.models import Users
from rest_framework import serializers

class ProductManager(models.Manager):
    def update_product(self, data):
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        price = data.get('price')
        product_to_update = Products.objects.filter(product_name=product_name).first()
        if product_to_update:
            if quantity:
                product_to_update.quantity = quantity
            if price:
                product_to_update.price = price
            product_to_update.save()
            return True
        else:
            raise serializers.ValidationError("No product with that name to update")

class Products(models.Model):
    # class Meta:
    #     unique_together = (('product_id','product_name'),)

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False, unique=True)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False, default=1)
    added_by = models.ForeignKey(Users, on_delete=models.CASCADE)

    objects = ProductManager()
