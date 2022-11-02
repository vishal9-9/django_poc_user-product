from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import AdminRegistrationView, UserRegistrationView, UserLoginView, UserListView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/register/', AdminRegistrationView.as_view()),
    path('user/register/',UserRegistrationView.as_view()),
    path('user/login/',UserLoginView.as_view()),
    path('user/',UserListView.as_view()),
]
