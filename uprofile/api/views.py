from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from uprofile.models import Profile
from django.contrib.auth.models import User
from django.conf import settings
from tweets.models import Tweet
from tweets.serializers import TweetSerializer,TweetActionSerializer,TweetCreateSerializer
import random
from django.utils.http import is_safe_url
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.db.models import Q
from uprofile.serializers import PublicProfileSerializer
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# @api_view(['GET','POST'])#http method that the client has to send
# # @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def user_follow(request,username):
# 	'''
# 	NORMAL DJANGO
# 	'''
# 	# if not request.user.is_authenticated:
# 	# 	if request.is_ajax():
# 	# 		return Response({},status=401)
# 	# 	return redirect(settings.LOGIN_URL)
# 	# form = TweetForm(request.POST or None)
# 	# next_url = request.POST.get('next') or None
# 	# print("next_url",next_url)
# 	# if form.is_valid():
# 	# 	obj = form.save(commit = False)
# 	# 	user = request.user
# 	# 	obj.user = user
# 	# 	obj.save() 
# 	# 	if request.is_ajax():
# 	# 		return Response(obj.serialize(),status=201)
# 	# 	if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
# 	# 		return redirect(next_url)
# 	# 	form = TweetForm()
# 	# if form.errors:
# 	# 	if request.is_ajax():
# 	# 		return Response(form.errors,status = 400)
# 	# return render(request,'components/form.html',context = {'form':form})
# 	'''
# 	DJANGO REST FRAMEWORK
# 	'''

# 	me = request.user
# 	other_user = User.objects.filter(username=username)
# 	if not other_user.exists():
# 		return Response({},status=400)
# 	other_user = other_user.first()
# 	if me.username == other_user.username :
# 		account = PublicProfileSerializer(me.profile , many=False , context={'request':request})
# 		return Response(account.data,status=200)
# 	data = request.data or {}
# 	action = data.get("action")
# 	profile = other_user.profile
# 	print(data)
# 	if action=='follow':
# 		profile.followers.add(me)
# 	elif action=='unfollow':
# 		profile.followers.remove(me)
# 	account = PublicProfileSerializer(profile , many=False ,context={'request':request})
# 	return Response(account.data,status=200)


@api_view(['GET','POST'])
def profile_view(request,username):
	qs = Profile.objects.filter(user__username=username)
	if not qs.exists():
		return Response({"detail":"user not found"},404)
	profile = qs.first()
	data = request.data or {}
	action = data.get("action")
	if request.method =='POST':
		me = request.user
		if me != profile.user:
			if action=='follow':
				profile.followers.add(me)
			elif action=='unfollow':
				profile.followers.remove(me)
	prof = PublicProfileSerializer(profile,many=False,context={'request':request})
	return Response(prof.data,200)

