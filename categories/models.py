from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
