from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import CommentForm
from .models import Post


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-created_time"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset[:3]
        return queryset


class PostListView(ListView):
    template_name = "blog/post-list.html"
    model = Post
    ordering = ["-created_time"]
    context_object_name = "posts"


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.order_by("-id"),
        }

        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.order_by("-id"),
        }

        return render(request, "blog/post-detail.html", context)
