"""sheringhamportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.urls import include,path

app_name = 'eroicamildmay'



urlpatterns = [
    path('', views.twhome, name='index'),
    path('falling/', views.falling, name='porthome'),
    path('tele/', views.tele, name='porthome'),
    path('colours/', views.col_change, name='porthome'),
    path('home/', views.twhome, name='porthome'),
    path('about', views.twabout, name='porthome'),
    path('past', views.twPast, name='porthome'),
    path('about/', views.twabout, name='porthome'),
    path('/about', views.twabout, name='porthome'),
    path(r'^$', views.twabout, name='porthome'),
    path('twwdabout', views.twabout, name='porthome'),
    path('contact', views.twcontact, name='porthome'),


]
