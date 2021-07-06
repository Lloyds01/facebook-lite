from posts.models import Comment, Like,Post
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)