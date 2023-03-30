from rest_framework import serializers
from .models import Category
from users.serializers import TinyUserSerializer


class CategorySerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Category
        exclude = (
            "created_at",
            "updated_at",
        )
