from django.shortcuts import render
from app.models import Subreddit, Post, Comment
from app.forms import SubForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

# Create your views here.

class SubredditListView(ListView):
    template_name = "index.html"
    model = Subreddit

class PostListView(ListView):
    template_name = "posts.html"
    model = Post
    def get_queryset(self):
        var = super(PostListView, self).get_queryset()
        return var.filter(subreddit_id=self.kwargs['sub_id'])

class PostDetailView(DetailView):
    model = Post

class CommentCreateView(CreateView):
    model = Comment
    success_url = "/"
    fields = ('comment_text',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail_view",args=[int(self.kwargs['pk'])])
