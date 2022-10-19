from rest_framework import serializers

from user.models import User, Users, Admin

class AdminRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input-type':'password'}, write_only=True)

    class Meta:
        model=Admin
        fields=['email','name','password','confirm_password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        del validated_data['confirm_password']
        return Users.object.create_superuser(**validated_data)

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input-type':'password'}, write_only=True)

    class Meta:
        model=User
        fields=['name','email','password','confirm_password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Password so not match')

        return attrs

    def create(self, validated_data):
        del validated_data['confirm_password']
        return Users.object.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model=Users
        fields=['email','password']
