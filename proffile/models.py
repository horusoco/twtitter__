from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

class Contact(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='rel_from_set',
                                    on_delete=models.CASCADE)
    user_to = models.ForeignKey(User,
                                    related_name='rel_to_set',
                                    on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                    db_index=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return '{} follows {}'.format(self.user_from,
                                                 self.user_to)

User.add_to_class('following',
                            models.ManyToManyField('self',
                                                    through=Contact,
                                                    related_name='followers',
                                                    symmetrical=False))   
                                   

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    friends = models.ManyToManyField("Profile", blank=True)                            
    date_of_birth = models.DateField(blank=True,
                                     null=True)
    photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d',
                                blank=True,
                                default='static/css/not-found.png')
    cover_picture = models.ImageField(upload_to='page_photo/%Y/%m/%d',
                                blank=True,
                                default='static/not-found.png')
    country = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
  
    date_joinded = models.DateField(auto_now_add=True)
    # following iyo followers for field name kumma isticmaali karno modelkan profileka maadaama ay same name 
    # noqonayaan User modelka oo aynu galinay following/fowwowers field names 
    #sababtuna waa profileka ayaa related ku ah User modelka 
    followwing = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='followwers',
                                        blank=True
                                    )

    def __str__(self):
        return self.user.username
   

    # @property
    # def profile_photo(self):
    #     if self.photo.url:
    #         return self.photo.url
    #     else:
    #         return 'upload a photo'



 