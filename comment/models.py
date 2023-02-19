from django.db import models
from common.models import CommonModel


class Comment(CommonModel):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        "posts.Post",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    payload = models.TextField()
    c_like = models.PositiveIntegerField(null=True, default="0")
    c_dislike = models.PositiveIntegerField(null=True, default="0")

    def like_count(self):
        return Comment.c_like.count()

    def dislike_count(self):
        return Comment.c_dislike.count()
