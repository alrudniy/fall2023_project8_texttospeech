from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('history', views.history, name='history'),
    path('mainapp', views.mainapp, name = 'mainapp'),
    path('profile', views.profile,name="profile"),
    path('text_to_speech',views.text_to_speech,name='text_to_speech'),
]
