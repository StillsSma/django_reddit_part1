from django.contrib import admin

# Register your models here.
from app.models import Subreddit, Post, Comment
admin.site.register(Subreddit)
admin.site.register(Post)
admin.site.register(Comment)
