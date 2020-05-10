from django.shortcuts import render
from . forms import PostFormTweet

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