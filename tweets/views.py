from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Tweet
from django.conf import settings
import random
from .forms import TweetForm
from django.utils.http import is_safe_url
from .serializers import TweetSerializer,TweetActionSerializer,TweetCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
	user = User.objects.all()
	user = user.values_list('username',flat=True)
	return Response({'user':user})

def home(request):
	return render(request,'tweets/feed.html',status=200)


def search(request):
	if request.user.is_authenticated:
		return render(request,'pages/search.html')
	return redirect('auth/login')

@api_view(['GET'])
def tweet_detail(request,pk):
	# # tweet  = get_object_or_404(Tweet,id=pk)
	# data={ "id":pk  }
	# status = 200
	# try:
	# 	tweet = Tweet.objects.get(id=pk)
	# 	data['tweet'] = tweet.tweet
	# except:
	# 	data['message'] = "not found"
	# 	status = 404
	# return Response(data,status = status)
	tweet  = Tweet.objects.filter(id=pk)
	print(pk,'pk')
	if not tweet.exists():
		return Response({},status = 404)
	obj = tweet.first()
	serializer = TweetSerializer(obj)
	return Response(serializer.data,status=200)

@api_view(['GET'])
def tweet_list(request):
	# tweets = Tweet.objects.all()
	# tweets_list = [ x.serialize() for x in tweets]
	# data={
	# 	"response":tweets_list
	# }
	# return Response(data)
	tweets  = Tweet.objects.all()
	user = request.GET.get('username')
	print(user,'Users')
	qs={}
	if user!=None:
		qs = tweets.filter(user__username__iexact= user)
	else:
		qs=tweets
	return paginated_response(qs,request)





@api_view(['POST'])#http method that the client has to send
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create(request):
	'''
	NORMAL DJANGO
	'''
	# if not request.user.is_authenticated:
	# 	if request.is_ajax():
	# 		return Response({},status=401)
	# 	return redirect(settings.LOGIN_URL)
	# form = TweetForm(request.POST or None)
	# next_url = request.POST.get('next') or None
	# print("next_url",next_url)
	# if form.is_valid():
	# 	obj = form.save(commit = False)
	# 	user = request.user
	# 	obj.user = user
	# 	obj.save() 
	# 	if request.is_ajax():
	# 		return Response(obj.serialize(),status=201)
	# 	if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
	# 		return redirect(next_url)
	# 	form = TweetForm()
	# if form.errors:
	# 	if request.is_ajax():
	# 		return Response(form.errors,status = 400)
	# return render(request,'components/form.html',context = {'form':form})
	'''
	DJANGO REST FRAMEWORK
	'''

	serializer = TweetCreateSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save(user = request.user)
		print(serializer.data)
		return Response(serializer.data,status=201)
	return Response({},status=400)


def paginated_response(qs,request):
	paginator = PageNumberPagination()
	paginator.page_size = 20
	paginated_qs = paginator.paginate_queryset(qs,request)
	serializer = TweetSerializer(paginated_qs,many=True)
	return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tweet_feed(request):
	# tweets = Tweet.objects.all()
	# tweets_list = [ x.serialize() for x in tweets]
	# data={
	# 	"response":tweets_list
	# }
	# return Response(data)
	user = request.user
	qs = Tweet.objects.feed(user)
	return paginated_response(qs,request)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def tweet_delete(request,pk):
	tweet  = Tweet.objects.filter(id=pk)
	if not tweet.exists():
		return Response({},status=404)
	tweet = tweet.filter(user = request.user)
	if not tweet.exists():
		return Response({'message':'You cannot delete the tweet'},status = 401)
	obj = tweet.first()
	obj.delete()
	return Response({'messaage':'Successfully Deleted'} , status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action(request):
	# print(request.META)
	'''
	id is required
	Action options are like unlike and retweet
	'''
	print(request.data,request.POST)
	serializer = TweetActionSerializer(data=request.data)
	if serializer.is_valid():
		data = serializer.validated_data
		tweet_id = data.get('id')
		action = data.get('action')
		content = data.get('content')
		tweet = Tweet.objects.filter(id=tweet_id)
		print(serializer.data)
		if not tweet.exists():
			return Responsne({},status=404)
		obj = tweet.first()
		if obj.user == request.user:
			tweets = TweetSerializer(obj , many=False)
			return Response(tweets.data,status=200)
		if action == 'like':
			print("in")
			obj.likes.add(request.user)
		elif action == 'unlike':
			obj.likes.remove(request.user)
		else :
			parent = obj
			original_tweet= TweetSerializer(obj , many=False)
			new_tweet= Tweet.objects.create(user=request.user,parent=parent,tweet=content)
			serializer = TweetSerializer(new_tweet)
			if 'profile' in request.META['HTTP_REFERER']:
				return Response(original_tweet.data,status=200)
			print(serializer.data,'checking action')
			return Response(serializer.data,status=201)
		serializer = TweetSerializer(obj)
		print(serializer.data)
	return Response(serializer.data,status=200)

def list_view(request):
	return render(request,'tweets/list.html')


def detail_view(request,id):
	return render(request,'tweets/detail.html',{'tweetid':id})

