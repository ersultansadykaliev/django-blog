from django.urls import path
from.views import PostListView, PostDetailView, PostSearchView
from.feeds import LatestPostsFeed

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', PostSearchView.as_view(), name='post-search'),
    path('rss/', LatestPostsFeed(), name='post-rss'),
]