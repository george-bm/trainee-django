from base_app import views
from django.urls import path, include
from users.views import Speech, AddUser, DeleteUser

urlpatterns = [
    path('health', views.HeartBeatHealthCheck.as_view(), name='common_healthcheck'),
    path('users/', include('users.urls')),
    path('add_user', AddUser.as_view(), name='common_add_user'),
    path('delete_user', DeleteUser.as_view(), name='common_add_user')
]
