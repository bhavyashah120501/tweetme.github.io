from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.test import APIClient
# Create your tests here.


class ProfileTestCase(TestCase):
	def setUp(self):
		self.user1 = User.objects.create_user(username='cfe',password='somepassword')
		self.user2 = User.objects.create_user(username='bhavya',password='somepassword')

	def test_profile_created_via_signal(self):
		qs = Profile.objects.all()
		self.assertEqual(qs.count(),2)

	def get_client(self):
		client = APIClient()
		client.login(username=self.user1.username , password = 'somepassword')
		return client

	def test_following(self):
		first = self.user1
		second = self.user2

		first.profile.followers.add(second)
		qs = second.following.filter(user=first)
		self.assertTrue(qs.exists())
		first_no_one_following = first.following.all()
		self.assertFalse(first_no_one_following.exists())

	def test_follow_api_endpoint(self):
		client = self.get_client()
		response = client.post(
			f"/api/profile/{self.user2.username}/follow",
			{"action":"follow"}
			)
		data = response.json()
		count = data.get('followers')
		self.assertEqual(count,1)

	def test_unfollow_api_endpoint(self):
		first = self.user1
		second = self.user2
		second.profile.followers.add(first)
		client = self.get_client()
		response = client.post(
			f"/api/profile/{self.user2.username}/follow",
			{"action":"unfollow"}
			)
		data = response.json()
		count = data.get("followers")
		self.assertEqual(count,0)

	def test_cannot_follow(self):
		client = self.get_client()
		response = client.post(
			f"/api/profile/{self.user1.username}/follow",
			{"action":"follow"}
			)
		data = response.json()
		count = data.get('followers')
		self.assertEqual(count,0)