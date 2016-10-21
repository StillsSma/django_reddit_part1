"""reddit_remake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import SubredditListView, PostListView, PostDetailView, CommentCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', SubredditListView.as_view(), name="subreddit_list_view"),
    url(r'^subreddit/(?P<sub_id>\d+)/$', PostListView.as_view(), name="post_list_view"),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post_detail_view"),
    url (r'^create/comment/(?P<pk>\d+)$', CommentCreateView.as_view(), name="comment_create_view"),
]
