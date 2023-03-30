from .models import Category
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import CategorySerializer
from posts.serializers import PostListSerializer


class CategoryviewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_posts_by_category(self, request, pk):
        category = self.get_object()
        posts = category.posts.all()
        author = category.users.all()
        serializer = PostListSerializer(
            posts,
            author,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def get_serializer_context(self):
        return {"request": self.request}
