import logging, io, os

from google.cloud import speech
from google.cloud.speech import types

from base_app.utils.json import Json

logger = logging.getLogger(__name__)

class SpeechToText(Json):
    def post(self, request):

        # Instantiates a client
        client = speech.SpeechClient()

        # Loads the audio
        content = request.FILES['file'].read()
        audio = types.RecognitionAudio(content=content)

        # Config
        config = types.RecognitionConfig(
            encoding='FLAC',
            language_code='ru-RU')

        # Detects speech in the audio file
        response = client.recognize(config, audio)
        for result in response.results:
            text = result.alternatives[0].transcript

        logger.info('SpeechToText: ' + text)
        return dict(
            transcript=text
        )
