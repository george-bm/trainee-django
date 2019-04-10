import logging

from django.http import HttpResponseBadRequest
from django.http.response import JsonResponse
from django.views import View
from google.cloud import speech
from google.cloud.speech import types

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

        # Detects speech in the audio file
        response = client.recognize(config, audio)
        for result in response.results:
            text = result.alternatives[0].transcript
            confidence = result.alternatives[0].confidence

        logger.info('SpeechToText: ' + text)
        return JsonResponse({
            'transcript': text,
            'confidence': confidence
        })
