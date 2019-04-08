import logging, io, os

from django.http import HttpResponseBadRequest

from google.cloud import speech
from google.cloud.speech import types

from base_app.utils.json import Json

logger = logging.getLogger(__name__)

class SpeechToText(Json):
    def post(self, request):

        if not 'lang' in request.POST:
            return HttpResponseBadRequest('Please provide language code.')
        if not 'file' in request.FILES:
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
        return dict(
            transcript=text,
            confidence=confidence
        )
