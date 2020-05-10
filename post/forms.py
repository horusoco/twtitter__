from django import forms 
from . models import Post, Comment

class PostFormTweet(forms.ModelForm):
    # content = forms.Textarea(widget=forms.TextInput(attrs={'col':40, 'rows':50 ,'placeholder': 'What is happening'}), label='')
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'What is happening?' }))

    class Meta:
        model = Post
        fields = ('image','content')

class PostFormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
       