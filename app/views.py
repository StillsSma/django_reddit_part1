from django.shortcuts import render
from app.models import Subreddit, Post, Comment
from app.forms import SubForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

def index_view(request):
    if request.POST:
        instance = SubForm(request.POST)
        if instance.is_valid():
            instance.save()

    context = {
    'subreddit': Subreddit.objects.all(),
    'form': SubForm()

    }
    return render(request, 'index.html', context)

class SubredditView(ListView):
    template_name = "subreddits.html"
    model = Post
    def get_queryset(self):
        var = super(SubredditView, self).get_queryset()
        return var.filter(subreddit_id=self.kwargs['sub_id'])
