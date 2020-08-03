"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tweets import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',views.search,name='search'),
    path('',views.home,name='home'),
    path('api/',include('tweets.urls')),
    path('auth/',include('accounts.urls')),
    path('react/',TemplateView.as_view(template_name='react.html'),name='react'),
    path('global/',views.list_view,name='list'),
    path('profile/',include('uprofile.urls')),
    path('<int:id>',views.detail_view,name='detail'),
    path('api/profile/',include('uprofile.api.urls'))
]

if settings.DEBUG :
	urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)