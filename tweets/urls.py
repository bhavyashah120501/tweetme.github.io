from django.urls import path,include
from tweets import views

urlpatterns = [
    path('tweets/<int:pk>',views.tweet_detail,name='detail'),
    path('tweets',views.tweet_list,name = 'list'),
    path('tweet/create',views.tweet_create,name='create'),
    path('tweet/<int:pk>/delete',views.tweet_delete,name='delete'),
    path('tweets/action',views.tweet_action,name='action'),
    path('tweets/feed',views.tweet_feed,name="tweet_feed"),
    path('users' , views.users,name='users')
]
