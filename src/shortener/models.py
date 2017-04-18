import random
import string
from django.db import models

# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	# new_code = ''
	# for _ in range(size):
	# 	new_code += random.choice(chars)
	# return new_code

	return ''.join(random.choice(chars) for _ in range(size))


class KirrURL(models.Model):
	url 	  = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=15, unique=True)
	updated   = models.DateTimeField(auto_now=True) #every time model is saved set time value
	timestamp = models.DateTimeField(auto_now_add=True)
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	#shortcode = models.CharField(max_length=15, null=True) empty in database is ok
	#shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

	def save(self, *args, **kwargs):
		print("something")
		self.shortcode = code_generator()
		super(KirrURL, self).save(*args, **kwargs)

	def my_save(self):
		self.save()

	def __str__(self):
		return str(self.url)

	def __unicode__():
		return str(self.url)

'''
Making it sync with DB without migrations folder and db.sqlite3
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''