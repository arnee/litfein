from django.conf import settings
import os

MEDIA_PATH_PREFIX = settings.MEDIA_URL_PREFIX + settings.MEDIA_URL

def media_urls(request):
    return {
        "MEDIA_PATH_PREFIX": MEDIA_PATH_PREFIX,
    }
