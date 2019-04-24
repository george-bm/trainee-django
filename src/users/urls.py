from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from users.views import Users

urlpatterns = [
    path('users', Users.as_view(), name='common_users'),
    path('token', obtain_jwt_token),
]
