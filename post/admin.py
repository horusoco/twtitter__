from django.contrib import admin
from . models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Post,PostAdmin)


class CommentPost(admin.ModelAdmin):
    list_display = ('post',)

admin.site.register(Comment, CommentPost)