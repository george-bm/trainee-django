from base_app import views
from django.urls import path, include

urlpatterns = [
    path('health', views.HeartBeatHealthCheck.as_view(), name='common_healthcheck'),
    path('', include('users.urls')),
    path('', include('followers.urls')),
    path('', include('message.urls')),
]
