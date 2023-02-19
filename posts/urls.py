from django.urls import path
from . import views

urlpatterns = [
    path("", views.Posts.as_view()),
    path("<int:pk>", views.PostDetail.as_view()),
    path("<int:pk>/comments", views.PostComments.as_view()),
    path("<int:pk>/photos", views.PostPhotos.as_view()),
]
