from django import forms

from .models import Tweet
from django.conf import settings

MAX_LENGTH = settings.MAX_LENGTH_TWEET

class TweetForm(forms.ModelForm):

	class Meta:
		model = Tweet
		fields = ['tweet']
	def clean_tweet(self):
		MAX_LENGTH  = 240
		content = self.cleaned_data.get("tweet")
		print('content',content)
		if(len(content)> MAX_LENGTH):
			raise forms.ValidationError("This Tweet is too long")
		else:
			return  content
