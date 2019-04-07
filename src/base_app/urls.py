from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from base_app import views

urlpatterns = [
    url('health', views.HeartBeatHealthCheck.as_view(), name='common_healthcheck'),
    url('speechtotext', csrf_exempt(views.SpeechToText.as_view()), name='common_speechtotext'),
]
