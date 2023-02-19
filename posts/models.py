from django.db import models
from common.models import CommonModel

# Create your models here.
class Post(CommonModel):

    title = models.CharField(
        max_length=20,
        default="",
    )
    description = models.TextField()
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="posts",
    )
    p_like = models.PositiveIntegerField(null=True, default="0")
    p_dislike = models.PositiveIntegerField(null=True, default="0")

    def __str__(self) -> str:
        return self.title

    def like_count(post):
        return Post.p_like.count()

    def dislike_count(post):
        return Post.p_dislike.comment.count()
