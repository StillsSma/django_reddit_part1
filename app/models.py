from django.db import models
from django.conf import settings
from datetime import date,datetime, timedelta

# Create your models here.
class Subreddit(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    creation_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def current_count(self):
        return Post.objects.filter(subreddit__name=self.name).count()
    def today_count(self):
        yesterday = datetime.today() - timedelta(days=1)
        return Post.objects.filter(subreddit__name=self.name).filter(creation_time__gt=yesterday).count()
    def daily_average(self):
        start_time= datetime.today()- timedelta(days=6)
        end_time= datetime.today()
        return Post.objects.filter(creation_time__range=(start_time, end_time)).count()/7

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.URLField()
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    class Meta:
        ordering = ("-creation_time", )

    def __str__(self):
        return self.title

    def is_recent(self):
        return self.creation_time.date() == date.today()

    def is_hot(self):
        start_time = datetime.today() - timedelta(hours=3)
        end_time = datetime.today()
        return Comment.objects.filter(post__title=self.title).filter(creation_time__range=(start_time, end_time)).count() > 3

    def comments(self):
        return Comment.objects.filter(post=self)



class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


    def __str__(self):
        return self.comment_text
