from rest_framework import serializers
from .models import Tweet
from django.conf import settings
from uprofile.serializers import PublicProfileSerializer



MAX_LENGTH = settings.MAX_LENGTH_TWEET
TWEET_ACTION_OPTIONS=settings.TWEET_ACTION_OPTIONS
class TweetActionSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	action = serializers.CharField()
	content= serializers.CharField(allow_blank=True,required=False)
	class Meta:
		field:['id','action']
	def validate_action(self,value):
		value = value.lower().strip()
		if not value in TWEET_ACTION_OPTIONS:
			raise serializers.ValidationError('This is not a valid option')
		return value

class TweetCreateSerializer(serializers.ModelSerializer):
	likes = serializers.SerializerMethodField(read_only=True)
	user = PublicProfileSerializer(source='user.profile',read_only=True)
	class Meta:
		model = Tweet
		fields = ['id','tweet','likes','user','timestamp']

	def validate_tweet(self,value):
		if len(value) > MAX_LENGTH:
		    raise serializers.ValidationError('This tweet is too long')
		return value 

	def get_likes(self,object):
		return object.likes.count()




class TweetSerializer(serializers.ModelSerializer):
	likes = serializers.SerializerMethodField(read_only=True)
	tweet = serializers.SerializerMethodField(read_only=True)
	parent = TweetCreateSerializer(read_only=True)
	user = PublicProfileSerializer(source='user.profile',read_only=True)
	class Meta:
		model = Tweet
		fields = ['id','tweet','likes','parent','is_retweet','user','timestamp']


	def get_likes(self,object):
		return object.likes.count()

	def get_tweet(self,object):
		return object.tweet

		