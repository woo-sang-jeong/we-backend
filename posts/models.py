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
        "categories.Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(post) -> str:
        return post.title

    def like(post):
        count = post.comment.count()

    def dislike(post):
        count = post.comment.count()
