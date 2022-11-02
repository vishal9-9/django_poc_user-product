from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import Users
from user.serializers import AdminRegistrationSerializer, UserListSerializer, UserRegistrationSerializer, UserLoginSerializer

# Create your views here.

class AdminRegistrationView(APIView):
    def post(self, request):
        serialized_data = AdminRegistrationSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response({"status": 201, "success_message": "User created successfully"},status=201)
        return Response({"status": 400, "success_message": serialized_data.errors},status=400)

class UserRegistrationView(APIView):
    def post(self, request):
        serialized_data = UserRegistrationSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response({"status": 201, "success_message": "User created successfully"},status=201)
        return Response({"status": 400, "error_message": serialized_data.errors},status=400)

class UserLoginView(APIView):
    def post(self, request):
        serialized_data = UserLoginSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            email = serialized_data.data.get('email')
            password = serialized_data.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = RefreshToken.for_user(user=user)
                return Response({"status": 200, "success_message": {
                    "refresh": str(token),
                    "access_token": str(token.access_token),
                    "name": str(user.name),
                    "user_type": str(user.user_type),
                    "is_admin": str(user.is_admin),
                }},status=200)
            else:
                return Response({"status": 401, "error_message": "Invalid email or password"},status=401)

class UserListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        user_list = Users.objects.all()
        if user_list:
            to_return = []
            for user in user_list:
                serialized_data = UserListSerializer(user)
                to_return.append(serialized_data.data)
            return Response({"status": 200, "success_message": to_return},status=200)
        else:
            return Response({"status": 200, "success_message": "No user present"},status=200)
