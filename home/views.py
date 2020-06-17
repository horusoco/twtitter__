from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, \
                            HttpResponseRedirect, \
                                JsonResponse 
from django.views.generic.edit import DeleteView
from django.views.decorators.http import require_POST
from django.db.models import Q, Count
from django.urls import reverse
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

from post.models import Post, Comment
from post.forms import PostFormTweet,PostFormComment


# Create your views here.
@login_required
def home(request):
    # user = Post.objects.values('user__username').annotate(Count('user__username'))#another query
    # userada posaha ugu badan soo dhigay iyo tirada posaha ay soo dhigeen --> on the right side 
    users = User.objects.annotate(user_post=Count('user_posts')).order_by('-user_post')[:5]
    # user = User.objects.values('user_posts').annotate(Count('user_posts'))#onother query

    # home page users to follow on the right side
    users_to_follow = User.objects.exclude(username=request.user)[:6]
    # latest posts from all users 
    posts = Post.objects.all().order_by('-created')
    # for post in posts:
    #     pass
    #     if request.user not in post.users_like.all():
    #         post.users_like.add(request.user)
    #     else:
    #         post.users_like.remove(request.user)
    
    # search posts 
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
                            Q(title__icontains=query)|
                            Q(content__icontains=query)
                            ).distinct()
        return render(request, 'home.html', {'posts':posts,
                                        'query':query,
                                      })
    #tweet/posts form in the home page                                 
    if request.method == 'POST':
        form = PostFormTweet(data=request.POST,files=request.FILES)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.user = request.user        #sidana waad samaynkarkaa kaliya
            save_it.save()                     #form.instance.user = request.user
        #redirect same page                    #form.save() request.path_info
        return HttpResponseRedirect('/')
            
    else:
        form = PostFormTweet()
    context = {
                'posts':posts,
                'form':form,
                'users':users,
                'users_to_follow':users_to_follow,
        }
    
    
    return render(request, 'home.html',context)

# replay tweet
def give_post_tweet(request, id):
    posts = Post.objects.all()
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = PostFormComment(data=request.POST,files=request.FILES)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.post = post
            save_it.user = request.user        
            save_it.save() 
            
    else:
        form = PostFormComment()
    
    context = {
        'posts':posts,
        'post':post,
        'comments':comments,
        'form':form
    }
    return render(request, 'give_post_tweet.html',context)
        
# sigle wuxuu ku shaqaynayaa laakiin home pageka marka la joogo 
# ma shaqaynaayo maadaama postu u baahantahay idga la like garaynayo 
# isku day inaad garato adoo home page jooga inaad like saarto postada aad doonto 

@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            post = Post.objects.get(id=image_id)
            
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

# like tani waa xaga home page oo waa like garayn kartaa lakiin pagegu 
# wuxuu samaynayaa load markasta uu load sameeyana all post like ayay helayaaan
# garo sidii aad u samaynlahayd like for each post 
def like(request):
    posts = Post.objects.all()
    for post in posts:
        if request.user not in post.users_like.all():
            post.users_like.add(request.user)
        else:
            post.users_like.remove(request.user)
    return HttpResponseRedirect(reverse('home'))

def login(request):
    return render(request, 'registration/login.html', {})



def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post':post})