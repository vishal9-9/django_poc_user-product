from django.urls import path

from product.views import ProductCreationView, ProductUpdatingView

urlpatterns = [
    path('product/', ProductCreationView.as_view()),
    path('product/update/', ProductUpdatingView.as_view())
]
