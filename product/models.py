from django.db import models

from user.models import Users

# Create your models here.

class Products(models.Model):
    # class Meta:
    #     unique_together = (('product_id','product_name'),)

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False, unique=True)
    price = models.FloatField(null=False)
    added_by = models.ForeignKey(Users, on_delete=models.CASCADE)
