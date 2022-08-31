from django.urls import path

from .views import IndexView, PostDetailView, PostListView, ReadLaterView

app_name = "blog"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("read-later/", ReadLaterView.as_view(), name="read-later"),
]
