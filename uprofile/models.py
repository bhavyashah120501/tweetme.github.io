from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class FollowerRelation(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	profile = models.ForeignKey("Profile",on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	location = models.CharField(max_length=1000,blank=True,null=True)
	bio = models.TextField(blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	followers = models.ManyToManyField(User,related_name='following',blank=True,through=FollowerRelation)



def user_did_save(sender,instance,created,*args,**kwargs):
	if created:
	    Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save,sender=User)
