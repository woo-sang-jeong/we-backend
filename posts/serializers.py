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
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_like(self, post):
        return post.p_like()

    def get_dislike(self, post):
        return post.p_dislike()

    def get_is_owner(self, post):
        request = self.context.get("request")
        if request:
            return post.owner == request.user


class PostListSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)
    category = CategorySerializer(
        read_only=True,
    )

    class Meta:
        model = Post
        fields = (
            "pk",
            "category",
            "title",
            "p_like",
            "p_dislike",
            "owner",
            "is_owner",
            "photos",
        )

    def get_like(self, post):
        return post.p_like()

    def get_dislike(self, post):
        return post.p_dislike()

    def get_is_owner(self, post):
        request = self.context["request"]
        return post.owner == request.user
