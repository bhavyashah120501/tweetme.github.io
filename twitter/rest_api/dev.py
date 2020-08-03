from rest_framework import authentication
from django.contrib.auth import get_user_model

User = get_user_model()

class DevAuthentication(authentication.BasicAuthentication):
	def authenticate(self,request):
		qs = User.objects.all()
		user  = qs.filter(id=1).first()
		return (user,None)