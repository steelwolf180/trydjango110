from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitURLForm
from .models import KirrURL

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)
	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitURLForm()
		context = {
			"title": "Kirr.co",
			"form": the_form
		}
		return render(request, "shortener/home.html", context) #Try Django 1.8 & 1.9 http://joincfe.com/youtube

	def post(self, request, *args, **kwargs):
		form = SubmitURLForm(request.POST)
		context = {
			"title": "Kirr.co",
			"form": form
		}
		template = "shortener/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"created": created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		return render(request, template, context)

class KirrCBView(View):#class based view CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)

'''
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
	#print(request.user)
	#print(request.user.is_authenticated())
	print('method is \n')
	print(request.method)
	#obj = KirrURL.objects.get(shortcode=shortcode)

	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	# obj_url = obj.url 
	# try:
	# 	obj = KirrURL.objects.get(shortcode=shortcode)
	# except:
	# 	obj = KirrURL.objects.all().first()

	# obj_url = None
	# qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url 

	return HttpResponse("Hello {sc}".format(sc=obj.url))

class KirrCBView(View):#class based view CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponse("Hello again {sc}".format(sc=shortcode))

	def post(self, request, *args, **kwargs):
		return HttpResponse()
'''