import logging

from django.http import HttpResponseBadRequest, HttpResponse
from django.views import View
from users.models import User

from .models import Follower

logger = logging.getLogger(__name__)


class Follow(View):
    def post(self, request):
        if 'user_id' not in request.POST:
            return HttpResponseBadRequest('Please provide user_id.')
        if 'follow_id' not in request.POST:
            return HttpResponseBadRequest('Please provide follow_id.')

        user_id = request.POST['user_id']
        follow_id = request.POST['follow_id']

        if not User.objects.filter(id=user_id).exists():
            return HttpResponseBadRequest('No such user with id {}'.format(user_id))
        if not User.objects.filter(id=follow_id).exists():
            return HttpResponseBadRequest('No such user with id {}'.format(follow_id))

        if Follower.objects.filter(user_id=user_id, follow_id=follow_id).exists():
            return HttpResponseBadRequest('Already followed')

        Follower.objects.create(
            user_id=user_id,
            follow_id=follow_id,
        )
        return HttpResponse('Followed Successfully')

    def delete(self, request, user_id, follow_id):
        if not Follower.objects.filter(user_id=user_id, follow_id=follow_id).exists():
            return HttpResponseBadRequest('No such follow')

        Follower.objects.filter(user_id=user_id, follow_id=follow_id).delete()
        return HttpResponse('Unfollowed Successfully')
