from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.CategoryviewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "/<int:pk>",
        views.CategoryviewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "/<int:pk>/posts/",
        views.CategoryviewSet.as_view(
            {
                "get": "get_posts_by_category",
            }
        ),
    ),
]
