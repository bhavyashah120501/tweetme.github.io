from django.urls import path,include
from uprofile import views

urlpatterns = [
    path('<str:username>' , views.profile_view,name='profile_view'),
    path('user/edit',views.profile_update,name='profile_update')
]
