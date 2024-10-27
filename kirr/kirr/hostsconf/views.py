from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_REDIRECT_PATH = getattr(settings, 'DEFAULT_REDIRECT_PATH', 'http://www.kirr.co:8000')
def wildcard_redirect(request, path=None):
    if path is not None:
        new_url = DEFAULT_REDIRECT_PATH + "/" + path
    return HttpResponseRedirect(new_url)