import logging

from django.http import HttpResponseBadRequest, HttpResponse
from django.db import IntegrityError
from django.views import View
from users.models import User
import os
import settings

from .models import Message as MessageModel

logger = logging.getLogger(__name__)


class Message(View):
    def post(self, request):
        if 'user_id' not in request.POST:
            return HttpResponseBadRequest('Please provide user_id.')
        if 'text' not in request.POST:
            return HttpResponseBadRequest('Please provide text.')

        ext = os.path.splitext(request.FILES['file'].name)[1]
        if not ext.lower() in settings.VALID_EXTENSIONS:
            return HttpResponse('Unsupported file extension.')

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

