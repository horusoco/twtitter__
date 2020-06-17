from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('tweetpost/<id>', views.give_post_tweet, name='give_post_tweet'),
    path('like/', views.image_like, name='like'),
    path('detail/<id>', views.post_detail, name='post_detail'), #post detail for testing like button working

]