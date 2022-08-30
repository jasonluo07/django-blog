from django.urls import path

from .views import IndexView, PostDetailView, PostListView

app_name = "blog"
urlpatterns = [
    path("", IndexView.as_view(), name="index-page"),
    path("posts/", PostListView.as_view(), name="post-list-page"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post-detail-page"),
]
