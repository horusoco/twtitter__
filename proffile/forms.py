from django import forms 
from . models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ('cover_picture', 'photo',
                    'country', 'link','description', 'date_of_birth',)