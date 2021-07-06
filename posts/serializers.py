from django.db.models import fields
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Comment, Post, Like

class PostSerializer(ModelSerializer):
    likes = IntegerField(source="get_num_like",read_only = True)
    comment = IntegerField(source="get_num_comment",read_only=True)
    username = CharField(source="user.username",read_only=True)
    class Meta:
        model = Post
        fields =["text", "likes","created_on","comment","username"]

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["post", "user"]

class Commentserializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post","user"]