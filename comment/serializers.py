from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "user",
            "payload",
            "like",
            "dislike",
        )
