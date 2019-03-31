from django import forms 
from .models import contact
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class contactForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
	class Meta:
		model = contact
		fields = [
		'Email_id', 
		'First_name', 
		'Last_name',
		'phone_number'
		]


class Homeform(forms.ModelForm):
	post=forms.CharField()