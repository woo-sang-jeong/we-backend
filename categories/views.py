from .models import Category
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer


class CategoryviewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
