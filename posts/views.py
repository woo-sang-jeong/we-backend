from django.conf import settings
from django.utils import timezone
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Post
from categories.models import Category
from . import serializers
from comment.serializers import CommentSerializer
from medias.serializers import PhotoSerializer


class Posts(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_posts = Post.objects.all()
        serializer = serializers.PostListSerializer(
            all_posts,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PostDetailSerializer(data=request.data)
        if serializer.is_valid():
            category = request.data.get("category")
            if not category:
                raise ParseError("Category is required")
            post = serializer.save(
                owner=request.user,
                category=category,
            )
            serializer = serializers.PostDetailSerializer(
                post, context={"request": request}
            )
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class PostDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = serializers.PostDetailSerializer(
            post,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        if post.owner != request.user:
            raise PermissionDenied
        serializer = serializers.PostDetailSerializer(
            post,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            post = serializer.save()
            serializer = serializers.PostDetailSerializer(post)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post.owner != request.user:
            raise PermissionDenied
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class PostComments(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = CommentSerializer(
            post.comment.all(),
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(
                user=request.user,
                post=self.get_object(pk),
            )
            serializer = CommentSerializer(comment)
            return Response(serializer.data)

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass


class PostPhotos(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, pk):
        post = self.get_object(pk)
        serializer = PhotoSerializer(
            post.photos.all(),
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        post = self.get_object(pk)
        if request.user != post.owner:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(post=post)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
