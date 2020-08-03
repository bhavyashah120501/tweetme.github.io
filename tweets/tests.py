from django.test import TestCase
from .models import Tweet
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
# Create your tests here.

User = get_user_model()
class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe',password='somepassword')
        Tweet.objects.create(tweet ='my first tweet',user = self.user)
        Tweet.objects.create(tweet ='my second tweet',user = self.user)
        Tweet.objects.create(tweet ='my third tweet',user = self.user)
        Tweet.objects.create(tweet ='my fourth tweet',user = self.user)

    def test_tweet_created(self):
        tweet  = Tweet.objects.create(user = self.user,tweet="test")
        self.assertEqual(tweet.id,5)
        self.assertEqual(tweet.user,self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username,password='somepassword')
        return client

    def get_count(self):
        return Tweet.objects.all().count()

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/api/tweets")
        self.assertEqual(response.status_code,200)
        print(response.json())

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/tweets/action",{"id":1,"action":"like"})
        response = client.post("/api/tweets/action",{"id":1,"action":"unlike"})
        likes_count = response.json().get('likes')
        self.assertEqual(response.status_code,200)
        print(response.json(),likes_count)

    def test_action_retweet(self):
        client = self.get_client()
        response = client.post("/api/tweets/action",{"id":3,"action":"retweet","content":"neww"})
        self.assertEqual(response.status_code,200)
        current  = self.get_count()
        data = response.json()
        id = data.get('id')
        print("after")
        print(id)

    def test_tweet_create(self):
        data ={'tweet':'this is my test tweet','user':self.user }
        client = self.get_client()
        response = client.post("/api/tweet/create",data)
        self.assertEqual(response.status_code,201)
        data = response.json()
        id = data.get("id")
        print(id,'creates')
        # self.assertEqual(self.get_count() +1,id)

    def test_detail(self):
        client = self.get_client()
        response = client.get("/api/tweets/1")
        data = response.json()
        id = data.get('id')
        self.assertEqual(response.status_code,200)
        self.assertEqual(id,1)

    def test_delete(self):
        client = self.get_client()
        response = client.delete('/api/tweet/1/delete')
        self.assertEqual(response.status_code,200)
        






















