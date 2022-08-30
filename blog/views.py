from django.views.generic import DetailView, ListView

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


class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context
