from django.conf.urls import url

from base_app import views

urlpatterns = [
    url('health', views.HeartBeatHealthCheck.as_view(), name='common_healthcheck'),
    url('speechtotext', views.SpeechToText.as_view(), name='common_speechtotext'),
]
