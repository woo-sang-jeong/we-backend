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
    like = models.PositiveIntegerField()
    dislike = models.PositiveIntegerField()
