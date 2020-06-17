from django.shortcuts import render, get_object_or_404
from . forms import PostFormTweet
from .models import Post 

def create(request):
    if request.method == POST:
        form = PostFormTweet(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user 
            form.save()
    else:
        from = PostFormTweet()
    return render(request, 'post_form_tweet.htm',
                            {'form':from})    


