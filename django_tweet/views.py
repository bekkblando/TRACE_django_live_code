from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse

# NOTICE: django_tweet should be your app name
from django_tweet.models import Tweet

# Create your views here.


class TweetCreate(CreateView):
    model = Tweet
    fields = ["tweet_text"]
    success_url = 'list'


class TweetUpdate(UpdateView):
    model = Tweet
    fields = ["tweet_text"]
    success_url = 'detail'


class TweetDelete(DeleteView):
    model = Tweet
    success_url = "/tweet/list"


class TweetDetail(DetailView):
    model = Tweet


class TweetList(ListView):
    model = Tweet
