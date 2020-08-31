from django.forms import ModelForm
from .models import CV

class CVform(ModelForm):
	class Meta:
		model = CV
		fields = ['title','text']
        