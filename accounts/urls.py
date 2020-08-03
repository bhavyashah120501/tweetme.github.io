from django.urls import path,include
from accounts import views

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('registration',views.registration,name = 'registration')
]
