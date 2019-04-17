from django.urls import path, include
from users.views import AddUser, DeleteUser

urlpatterns = [
    path('add_user/', AddUser.as_view(), name='common_add_user'),
    path('delete_user/', DeleteUser.as_view(), name='common_add_user')
]
