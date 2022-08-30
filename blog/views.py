from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request):
    latest_posts = Post.objects.order_by("-created_time")[:3]
    context = {
        "posts": latest_posts,
    }

    return render(request, "blog/index.html", context)


def post_list(request):
    all_posts = Post.objects.order_by("-created_time")
    context = {
        "posts": all_posts,
    }

    return render(request, "blog/post-list.html", context)


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    context = {
        "post": identified_post,
    }

    return render(request, "blog/post-detail.html", context)
