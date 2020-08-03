from django.urls import path,include
from . import views

urlpatterns = [
    path('<str:username>/follow',views.profile_view,name='profile_view'),
    path('<str:username>',views.profile_view,name='profile_view')
]
