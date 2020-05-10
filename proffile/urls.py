from django.urls import path 
from . import views 

urlpatterns = [
	path('register/', views.signup, name='signup'),
    path('<username>/', views.user_profile, name='user_profile'),
    path('follow/', views.like, name='user_follow'),
    path('delete/<pk>/', views.DeletePost.as_view(), name='delete'),
    
       
]