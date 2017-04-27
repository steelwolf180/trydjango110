from django import forms

from .validators import validate_url, validate_dot_com

class SubmitURLForm(forms.Form):
	url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])

	# def clean(self):
	# 	cleaned_data = super(SubmitURLForm, self,).clean()
	# 	print(cleaned_data)
	# 	url = cleaned_data.get('url')
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URL for this field")
	# 	return url
	# 	#print(url)

	# def clean_url(self):
	# 	url = self.cleaned_data['url']
	# 	#print(url)
	# 	if not "com" in url:
	# 		raise forms.ValidationError("This is not valid because no .com")
		# url_validator = validator()
		# try:
		# 	url_validator(url)
		# except:
		# 	raise forms.ValidationError("Invalid URL for this field")
		# return url