from django.urls import path

from posts.views import PostsView, PostView, PostLikeView

app_name = "articles"

urlpatterns = [
    path('post', PostView.as_view()),
    path('post/like', PostLikeView.as_view()),
    path('posts', PostsView.as_view()),
]
