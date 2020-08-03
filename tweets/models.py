from django.db import models
import  random
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class TweetQuerySet(models.QuerySet):
	def feed(self,user):
		profiles_exist = user.following
		followed_users_id=[]
		if profiles_exist:
			followed_users_id =  user.following.values_list("user__id",flat=True)
		return self.filter(Q(user__id__in = followed_users_id) | Q(user = user)).distinct().order_by("-timestamp")


class TweetManager(models.Manager):
	def  get_queryset(self,*args,**kwargs):
		return TweetQuerySet(self.model,using=self._db)
	def feed(self,user):
		return self.get_queryset().feed(user)

class TweetLike(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	tweet = models.ForeignKey("Tweet",on_delete = models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
	parent = models.ForeignKey("self",null=True,blank=True,on_delete=models.SET_NULL,related_name='prt')
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	likes = models.ManyToManyField(User,related_name='tweet_user',blank=True,through=TweetLike)
	tweet = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='tweets/images',blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = TweetManager()
	class Meta:
		ordering = ['-id']
	def serialize(self):
		return {
		'id':self.id,
		'tweet':self.tweet,
		'likes':random.randint(2,100)
		}
	@property
	def is_retweet(self):
		return  self.parent != None
	def __str__(self):
		return self.tweet