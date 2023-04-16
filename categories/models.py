from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.post

    def __str__(self) -> str:
        return self.author
