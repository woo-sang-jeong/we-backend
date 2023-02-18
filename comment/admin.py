from django.contrib import admin
from .models import Comment


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, comment):
        word = self.value()
        if word:
            return Comment.filter(payload__contains=word)
        else:
            comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
        "like",
        "dislike",
    )
    list_filter = (
        WordFilter,
        "like",
        "dislike",
        "post__category",
    )
