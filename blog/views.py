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
    def get_is_saved_post(self, request, post_id):
        saved_posts = request.session.get("saved_posts")
        if saved_posts and post_id in saved_posts:
            is_saved_post = True
        else:
            is_saved_post = False

        return is_saved_post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.order_by("-id"),
            "is_saved_post": self.get_is_saved_post(request, post.id),
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


class ReadLaterView(View):
    def get(self, request):
        saved_posts = request.session.get("saved_posts")
        context = {}

        if not saved_posts:
            context["posts"] = []
        else:
            posts = Post.objects.filter(id__in=saved_posts)
            context["posts"] = posts

        return render(request, "blog/saved-posts.html", context)

    def post(self, request):
        saved_posts = request.session.get("saved_posts")

        if not saved_posts:
            saved_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in saved_posts:
            saved_posts.append(post_id)
        else:
            saved_posts.remove(post_id)

        request.session["saved_posts"] = saved_posts

        return HttpResponseRedirect("/")
