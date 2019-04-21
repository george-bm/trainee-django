from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from message.views import Message

urlpatterns = [
    path('message', Message.as_view(), name='common_message'),
    re_path('message/(\d+)', Message.as_view(), name='common_delete_message')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
