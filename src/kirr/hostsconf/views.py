from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDRIECT_URL = getattr (settings, "DEFAULT_REDRIECT_URL", "http://www.tirr.co")

def wildcard_redirect(request, path=None):
	new_url = DEFAULT_REDRIECT_URL
	if path is not None:
		new_url = DEFAULT_REDRIECT_URL + "/" + path
	return HttpResponseRedirect(new_url)