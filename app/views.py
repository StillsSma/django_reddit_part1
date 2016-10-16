from django.shortcuts import render
from app.models import Subreddit, Post, Comment

# Create your views here.

def index_view(request):

    context = {
    'subreddit': Subreddit.objects.get(pk=3),
    'posts': Post.objects.all(),

    }
    return render(request, 'index.html', context)
