from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "owner",
        "category",
        "p_like",
        "p_dislike",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "owner",
        "category",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "=owner__username",
    )
