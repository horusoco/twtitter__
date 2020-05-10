from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, \
                   HttpResponseRedirect, \
                    JsonResponse
                        
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from .models import Profile 
from post.models import Post 



def user_profile(request, username=None):
    # userka profilekiisa 
    user = User.objects.get(username=username)
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
        'postss':postss
        
    }

    return render(request, 'user_profile.html', context)



def like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            user = User.objects.get(id=image_id)
            
            if action == 'like':
                user.following.add(request.user)
            else:
                user.following.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

# delete post/tweet from user profile 
class DeletePost(DeleteView):

    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse('user_profile', args=[self.object.user.username]) 

# new user register 
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



class SignUp(CreateView):
    template_name = 'user_register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.save()
        return redirect(reverse('user_profile', args=[new_user.username]))
