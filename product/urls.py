from django.urls import path

from product.views import ProductCreationView

urlpatterns = [
    path('product/', ProductCreationView.as_view())
]
