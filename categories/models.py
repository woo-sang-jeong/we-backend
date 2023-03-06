from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    name = models.CharField(max_length=50)
    post = models.ForeignKey(
        "posts.Post",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="categories",
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
