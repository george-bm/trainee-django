from django.urls import re_path, path
from followers.views import Follow

urlpatterns = [
    path('follow', Follow.as_view(), name='common_follow'),
    re_path('follow/(\d+)/(\d+)', Follow.as_view(), name='common_unfollow'),
]
