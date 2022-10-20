from rest_framework import serializers

from product.models import Products

class ProductCreationSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255)
    price = serializers.FloatField()

    class Meta:
        model=Products
        fields=['product_name','price']

    def validate(self, attrs):
        product_name = attrs.get('product_name')
        price = attrs.get('price')
        if not Products.objects.filter(product_name=product_name).exists():
            user = self.context.get('user')
            product = {
                'product_name': product_name,
                'price': price,
                'added_by': user,
            }
            Products.objects.create(**product)
            return attrs
        else:
            raise serializers.ValidationError("Product already registered")
