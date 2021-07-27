from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Comment, Like, Post
# Create your tests here.


class PostTests(APITestCase):
    def test_create_post(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        # post = Post.objects.create(text= "i am doing great in the land of america", user=user)

        url = reverse('post-list')
        data = {'post': 'DabApps',"user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)
        print("COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        # self.assertEqual(Post.objects.get().text, data["text"])
        # self.assertEqual(response_data['text'], data['text'])

# class LikeTests(APITestCase):
#     def test_create_like(self):
#         user = User.objects.create_user(username="lloyds", password= "forlan123")
#         post = Post.objects.create(text= "complete outfit from yours truly",user=user)
#         like = Post.objects.create(user=user,post=post)

#         url = reverse('post-detail',kwargs={"pk":like.id})
#         data = {"post":post.id,"like":like.id,"user":user.id}
#         response =self.client.post(url,data)
#         response_data= response.jsom()
#         print(response_data)