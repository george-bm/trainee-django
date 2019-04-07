import logging, io, os

from google.cloud import speech
from google.cloud.speech import types

from base_app.utils.json import Json

logger = logging.getLogger(__name__)

class SpeechToText(Json):
    def get(self, request):
        # Instantiates a client
        client = speech.SpeechClient()

        # The name of the audio file to transcribe
        file_name = os.path.join(
            os.path.dirname(__file__),
            'ru.flac')

        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        # Config
        config = types.RecognitionConfig(
            encoding='FLAC',
            language_code='ru-RU')

        # Detects speech in the audio file
        response = client.recognize(config, audio)
        for result in response.results:
            text = 'Transcript: {}'.format(result.alternatives[0].transcript)

        logger.info('SpeechToText:' + text)
        return dict(
            result=text
        )
