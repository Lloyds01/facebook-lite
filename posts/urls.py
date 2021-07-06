from posts.models import Comment
from django.db import router
from rest_framework import routers
from django.urls.conf import include
from django.urls import path
from posts.views import PostViewSet,CommentviewSet,LikeViewSet, index


router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r"comment",CommentviewSet)


urlpatterns = [
    path('index/', index),
    path("", include(router.urls))
]
