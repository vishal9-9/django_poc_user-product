from django.urls import path

from product.views import ProductCreationView, ProductUpdatingView

urlpatterns = [
    path('product/', ProductCreationView.as_view()),
    path('product/<id>', ProductUpdatingView.as_view())
]
