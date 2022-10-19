from django.db import models

from user.models import Users

# Create your models here.

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    added_by = models.ForeignKey(Users, on_delete=models.CASCADE)
