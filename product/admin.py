from django.contrib import admin
from django.contrib.auth.models import Group

from product.models import Products

# Register your models here.

admin.site.register(Products)
admin.site.unregister(Group)
