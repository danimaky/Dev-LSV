import datetime

from django.conf import settings
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


class LifeSpanTokenMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        if getattr(request, 'auth', None) is not None:
            tf = datetime.datetime.now() - request.auth.created.replace(tzinfo=None)
            time_difference_in_minutes = tf.total_seconds() / 60
            lifespan = getattr(settings, 'EXPIRING_TOKEN_LIFESPAN', None) or 30  # The token has 30 minutes to be in use
            if time_difference_in_minutes > lifespan:
                Token.delete(request.auth)
                return JsonResponse(data={"detail":"Token has expired"}, status=401, safe=False)
        # Code to be executed for each request/response after
        # the view is called.
        return response
