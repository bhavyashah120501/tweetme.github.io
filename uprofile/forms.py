from .models import Profile
from django.contrib.auth.models import User
from django import forms

class ProfileUpdateForm(forms.ModelForm):
	firstName=forms.CharField(required=False)
	lastName=forms.CharField(required=False)
	email=forms.CharField(required=False)
	class Meta:
		model=Profile
		fields=['location','bio']