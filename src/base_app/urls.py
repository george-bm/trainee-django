from django.urls import path

from src.base_app import views
from src.speech.views import Speech

urlpatterns = [
    path('health', views.HeartBeatHealthCheck.as_view(), name='common_healthcheck'),
    path('speech', Speech.as_view(), name='common_speech'),
]
