from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,
                                     null=True)
    photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d',
                                blank=True)
    cover_picture = models.ImageField(upload_to='page_photo/%Y/%m/%d',
                                blank=True)
    country = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
  
    date_joinded = models.DateField(auto_now_add=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='followers',
                                        symmetrical=False,
                                        blank=True)

    def __str__(self):
        return self.user.username
    
    def haye(self):
        return self.photo
    