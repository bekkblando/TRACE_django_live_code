"""django_twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_tweet.views import TweetCreate, TweetUpdate, TweetList, TweetDetail, TweetDelete


urlpatterns = [
    path('tweet/create', TweetCreate.as_view()),
    path('tweet/list', TweetList.as_view(), name="feed"),
    path('tweet/<pk>/edit', TweetUpdate.as_view(), name="update_tweet"),
    path('tweet/<pk>/delete', TweetDelete.as_view(), name="delete_tweet"),
    path('tweet/<pk>/detail', TweetDetail.as_view(), name="detail_tweet"),
    path('admin/', admin.site.urls),
]
