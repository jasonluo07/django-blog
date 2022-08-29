from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def post_list(request):
    return render(request, "blog/post-list.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
