import logging

from django.http import HttpResponseBadRequest, HttpResponse
from django.views import View

from .models import User

logger = logging.getLogger(__name__)


class AddUser(View):
    def post(self, request):
        if 'login' not in request.POST:
            return HttpResponseBadRequest('Please provide login.')
        if 'password' not in request.POST:
            return HttpResponseBadRequest('Please provide password.')
        if 'lang' not in request.POST:
            return HttpResponseBadRequest('Please provide language_code.')
        if User.objects.filter(login=request.POST['login']).exists():
            return HttpResponseBadRequest('User already exist.')

        User.objects.create(
            login=request.POST['login'],
            password=request.POST['password'],
            lang=request.POST['lang']
        )
        return HttpResponse('User Added Successfully')


class DeleteUser(View):
    def post(self, request):
        if 'login' not in request.POST:
            return HttpResponseBadRequest('Please provide login.')
        if not User.objects.filter(login=request.POST['login']).exists():
            return HttpResponseBadRequest('No such user.')
        User.objects.filter(login=request.POST['login']).delete()
        return HttpResponse('User Deleted Successfully')
