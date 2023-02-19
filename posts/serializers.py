from rest_framework import serializers
from .models import Post
from users.serializers import TinyUserSerializer
from comment.serializers import CommentSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


class PostDetailSerializer(serializers.ModelSerializer):
    owner = TinyUserSerializer(
        read_only=True,
    )
    is_owner = serializers.SerializerMethodField()
    category = CategorySerializer(
        read_only=True,
    )
    like = serializers.SerializerMethodField()
    dislike = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_like(self, post):
        return post.like()

    def get_dislike(self, post):
        return post.dislike()

    def get_is_owner(self, post):
        request = self.context.get("request")
        if request:
            return post.owner == request.user


class PostListSerializer(serializers.ModelSerializer):

    like = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "pk",
            "title",
            "like",
            "dislike",
            "is_owner",
            "photos",
        )

    def get_like(self, post):
        return post.like()

    def get_dislike(self, post):
        return post.dislike()

    def get_is_owner(self, post):
        request = self.context["request"]
        return post.owner == request.user
