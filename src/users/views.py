import logging

from django.http import HttpResponseBadRequest, HttpResponse
from django.http.response import JsonResponse
from django.views import View
from google.cloud import speech
from google.cloud.speech import types

from .models import User

logger = logging.getLogger(__name__)


class Speech(View):

    def post(self, request):

        if 'lang' not in request.POST:
            return HttpResponseBadRequest('Please provide language code.')
        if 'file' not in request.FILES:
            return HttpResponseBadRequest('Please provide audio file.')

        # Instantiates a client
        client = speech.SpeechClient()

        # Loads the audio
        content = request.FILES['file'].read()
        audio = types.RecognitionAudio(content=content)

        # Config
        config = types.RecognitionConfig(
            encoding='FLAC',
            language_code=request.POST['lang'])

        # Detects users in the audio file
        response = client.recognize(config, audio)
        for result in response.results:
            text = result.alternatives[0].transcript
            confidence = result.alternatives[0].confidence

        logger.info('SpeechToText: ' + text)
        return JsonResponse({
            'transcript': text,
            'confidence': confidence
        })


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
