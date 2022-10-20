from rest_framework import serializers

from product.models import Products

class ProductCreationSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()
    price = serializers.FloatField()

    class Meta:
        model=Products
        fields=['product_name','price']

    def validate(self, attrs):
        product_name = attrs.get('product_name')
        quantity = attrs.get('quantity')
        price = attrs.get('price')
        if not Products.objects.filter(product_name=product_name).exists():
            user = self.context.get('user')
            product = {
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'added_by': user,
            }
            Products.objects.create(**product)
            return attrs
        else:
            raise serializers.ValidationError("Product already registered")

class ProductUpdatingSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(required=False)
    price = serializers.FloatField(required=False)

    class Meta:
        model=Products
        fields=['product_name']

    def validate(self, attrs):
        product_name = attrs.get('product_name')
        quantity = attrs.get('quantity')
        price = attrs.get('price')
        product_to_update = Products.objects.filter(product_name=product_name).first()
        if product_to_update:
            if quantity:
                product_to_update.quantity = quantity
            if price:
                product_to_update.price = price
            product_to_update.save()
        else:
            raise serializers.ValidationError("No product with that name to update")
        return attrs
