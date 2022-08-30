from django.contrib import admin

from .models import Author, Post, Tag


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("created_time",)
    list_display = (
        "full_name",
        "id",
        "first_name",
        "last_name",
        "email_address",
    )
    list_display_links = (
        "full_name",
        "id",
        "first_name",
        "last_name",
        "email_address",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = (
        "author",
        "tags",
        "created_time",
    )
    list_display = (
        "title",
        "author",
        "created_time",
    )
    list_display_links = (
        "title",
        "author",
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("created_time",)
    list_display = (
        "caption",
        "created_time",
    )
    list_display_links = ("caption",)
