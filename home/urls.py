from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('tweetpost/<id>', views.give_post_tweet, name='give_post_tweet'),
    path('like/', views.image_like, name='like'),
    ]