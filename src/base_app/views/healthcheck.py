import logging

from django.http.response import JsonResponse
from django.views import View

logger = logging.getLogger(__name__)


class HeartBeatHealthCheck(View):
    def get(self, request):
        logger.info('Common Health: OK')

        return JsonResponse({
            'result': 'CommonOK',
        })
