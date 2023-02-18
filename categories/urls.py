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
        "<int:pk>",
        views.CategoryviewSet.as_view(
            {
                "get": "retrive",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
