from base_app import views
from django.urls import path
from speech.views import Speech, AddUser, DeleteUser

urlpatterns = [
    path('health', views.HeartBeatHealthCheck.as_view(), name='common_healthcheck'),
    path('speech', Speech.as_view(), name='common_speech'),
    path('add_user', AddUser.as_view(), name='common_add_user'),
    path('delete_user', DeleteUser.as_view(), name='common_add_user')
]
