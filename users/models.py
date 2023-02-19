from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        ETC = ("etc", "Etc")

    login_id = models.CharField(
        max_length=30,
        editable=False,
    )
    avatar = models.URLField(blank=True)
    """
    name = models.CharField(
        max_length=20,
        default="",
    )
    """
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
