from posts.serializers import PostSerializer
from rest_framework.serializers import Serializer
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets,permissions
from .models import Comment, Post,Like
from .serializers import Commentserializer, LikeSerializer, PostSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello Liberty")

class PostViewSet(viewsets.ModelViewSet):
    '''
    Api endpoint taha allows user to be viewed or edited
    '''
    queryset=Post.objects.all()
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    '''
    API that allows viewers to like 
    '''
    queryset=Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes= [permissions.IsAuthenticated]


class CommentviewSet(viewsets.ModelViewSet):
    '''
    API for all trends available in the app 
    '''
    queryset = Comment.objects.all()
    serializer_class=Commentserializer