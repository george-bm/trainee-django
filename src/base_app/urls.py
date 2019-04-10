from django.urls import path

from base_app import views
from speech.views import Speech

urlpatterns = [
    path('health', views.HeartBeatHealthCheck.as_view(), name='common_healthcheck'),
    path('speech', Speech.as_view(), name='common_speech')
]
