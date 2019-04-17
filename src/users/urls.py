from django.urls import path, re_path
from users.views import Users

urlpatterns = [
    path('users', Users.as_view(), name='common_users'),
    re_path('users/(\w+)', Users.as_view(), name='common_delete_user')
]
