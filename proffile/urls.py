from django.urls import path 
from . import views 

urlpatterns = [
	path('register/', views.signup, name='signup'),
    path('edit/', views.editprofile, name='edit'),
    path('<username>/', views.user_profile, name='user_profile'),
    
    path('follow/', views.user_follow, name='user_follow'),
    path('delete/<pk>/', views.DeletePost.as_view(), name='delete'),
    path('followers/<username>/', views.users_followers, name='users_followers'),
    path('following/<username>/', views.users_following, name='users_following'),
    path('deletee/<id>/', views.deletee, name='deletee'),
   
    

    
       
]