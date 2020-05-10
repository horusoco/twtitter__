from django.db import models
from django.conf import settings
from django.urls import reverse



class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='user_posts')
    title = models.CharField(max_length=250,
                            blank=True)
    image = models.ImageField(upload_to='post_image/%Y/%m/%d',
                            blank=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='user_posts_like',
                                        blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or self.content 
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            related_name='user_comments')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)