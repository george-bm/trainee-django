import logging
import os

import settings
from django.db import IntegrityError
from django.http import HttpResponseBadRequest, HttpResponse
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User

from .models import Message as MessageModel

logger = logging.getLogger(__name__)


class Message(View):
    def post(self, request):
        if 'user_id' not in request.POST:
            return HttpResponseBadRequest('Please provide user_id.')
        if 'text' not in request.POST:
            return HttpResponseBadRequest('Please provide text.')
        if 'file' not in request.FILES:
            return HttpResponseBadRequest('Please provide file.')

        ext = os.path.splitext(request.FILES['file'].name)[1]
        if not ext.lower() in settings.VALID_EXTENSIONS:
            return HttpResponseBadRequest('Unsupported file extension.')

        user_id = request.POST['user_id']
        text = request.POST['text']
        file = request.FILES['file']

        try:
            if not User.objects.filter(id=user_id).exists():
                return HttpResponseBadRequest('No such user with id {}'.format(user_id))
        except ValueError:
            return HttpResponse('User id value error')

        try:
            MessageModel.objects.create(
                user_id=user_id,
                text=text,
                file=file,
            )
            return HttpResponse('Message Added Successfully')
        except ValueError:
            return HttpResponse('Value error')
        except IntegrityError:
            return HttpResponse('Integrity Error')

    def delete(self, request, id):
        if not MessageModel.objects.filter(id=id).exists():
            return HttpResponseBadRequest('No such message.')
        MessageModel.objects.filter(id=id).delete()
        return HttpResponse('Message Deleted Successfully')

    def get(self, request):
        messages = list(MessageModel.objects.all().values_list('id', 'text', 'file'))
        return JsonResponse({'messages': messages})
