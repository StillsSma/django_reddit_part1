from django.shortcuts import render
from app.models import Subreddit, Post, Comment
from app.forms import SubForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

# Create your views here.

class SubredditListView(ListView):
    template_name = "index.html"
    model = Subreddit

class SubredditCreateView(CreateView):
    model = Subreddit
    fields = ('name', 'description')
    success_url = reverse_lazy('subreddit_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class SubredditDetailView(DetailView):
    model = Subreddit


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("subreddit_detail_view",args=[int(self.kwargs['pk'])])


class CommentCreateView(CreateView):
    model = Comment
    fields = ('comment_text',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail_view",args=[int(self.kwargs['pk'])])


class SubredditUpdateView(UpdateView):
    model = Subreddit
    fields = ('name', 'description')
    success_url = reverse_lazy('subreddit_list_view')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'description')
    success_url = reverse_lazy('post_detail_view')

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('comment_text',)
    success_url = reverse_lazy('post_detail_view')
