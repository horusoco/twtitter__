from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, \
                   HttpResponseRedirect, \
                    JsonResponse
                        
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import ProfileEditForm

from .models import Contact, Profile
from post.models import Post 

# new user register for function based views 
def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            new_user = signup_form.save(commit=False)
            new_user.set_password(signup_form.cleaned_data['password1'])

            new_user.save()
            return redirect(reverse('user_profile', args=[new_user.username]))
           

            
    else:
        signup_form = UserCreationForm()
    return render(request, 'user_register.html', {'signup_form':signup_form})


# new user register for class based views 
class SignUp(CreateView):
    template_name = 'user_register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.save()
        return redirect(reverse('user_profile', args=[new_user.username]))



def user_profile(request, username):
    # userka profilekiisa 

    user = User.objects.get(username=username)
    # user profile
    # profile = Profile.objects.get(user=user)
    # you might like users on right side user profile 
    users = User.objects.exclude(username=request.user.username)[:6]
    # userku  postsa/tweetka iyo images ka uu soo dhigay 
    user_posts = user.user_posts.all()
    # 6 latest posts images on the user profile on the  right side
    postss = user.user_posts.all().order_by('-created')[:6]  

    context = {
        'user':user,
        'users':users,
        'user_posts':user_posts,
        'postss':postss,
        # 'profile':profile
        
    }

    return render(request, 'user_profile.html', context)

# edit profile 
def editProfile(request,user):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        edit_profile_form = ProfileEditForm(instance=profile,
                                            data=request.POST,
                                            files=request.FILES)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return HttpResponseRedirect(reverse('user_profile', args=[request.user.username]))
    else:
        edit_profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'user_edit_profile.html', {'edit_profile_form': edit_profile_form})


# QAABKAN SARE IYO KAN HOOSE WAA ISKU MID KII AAD ISTICMAASHO, MID WAA ISAGOO 
# PARAMETER LEH MID WAA WITH OUT PARAMETER 
# edit profile 
def editprofile(request):
    if request.method == 'POST':
        edit_profile_form = ProfileEditForm(instance=request.user.profile,
                                            data=request.POST,
                                            files=request.FILES)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return HttpResponseRedirect(reverse('user_profile', args=[request.user.username]))
    else:
        edit_profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'user_edit_profile.html', {'edit_profile_form': edit_profile_form})


# delete post/tweet from user profile 
class DeletePost(DeleteView):

    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse('user_profile', args=[self.object.user.username]) 

def deletee(request, id):
    user = request.user
    post = Post.objects.filter(id=id, user=user).delete()
    data = {
        'post':post
    }
    # return HttpResponseRedirect(reverse('user_profile', args=[request.user.username]))
    return HttpResponse(json.dumps(data), content_type='application/json')

# follow view using JsonResponse 
@require_POST
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,
                                                user_to=user)
            else:
                Contact.objects.filter(user_from=request.user,
                                                user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})

# following users 
def users_following(request, username):
    user = User.objects.get(username=username)
    user_following = user.following.all()

    

    context = {
        'user_following':user_following
    }
    return render(request, 'user_following.html',context)

# followers user 
def users_followers(request, username):
    user = User.objects.get(username=username)
    user_followers = user.followers.all()

    

    context = {
        'user_followers':user_followers
    }
    return render(request, 'user_followers.html',context)


