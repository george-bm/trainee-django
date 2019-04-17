from django.urls import path, include
from followers.views import Follow

urlpatterns = [
    path('follow/', Follow.as_view(), name='common_follow'),
]
