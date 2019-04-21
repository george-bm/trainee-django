from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from message.views import Message

urlpatterns = [
    path('message', Message.as_view(), name='common_follow'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
