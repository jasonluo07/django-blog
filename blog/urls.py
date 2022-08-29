from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index-page"),
    path("posts/", views.post_list, name="post-list-page"),
    path("posts/<slug:slug>/", views.post_detail, name="post-detail-page"),
]
