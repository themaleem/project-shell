from django.shortcuts import render
from .models import Post,Response
from .serializers import FeedSerializer

from rest_framework import viewsets,decorators
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response as Res

# get the anonymous user instance
# to prefill it in post requests
anon=User.objects.get(username='anonymous')

# class PostViewset(viewsets.ModelViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
#     lookup_field = 'pk'

#     @action(detail=True,methods=["GET"])
#     def responses(self,request,pk=None):
#         post=self.get_object()
#         responses=post.responses
#         serializer=PostResponseSerializer(responses,many=True)
#         return Res(serializer.data,status=200)


#     def perform_create(self,serializer):
#         print("***************")
#         print(self.request.user.is_anonymous)
#         print("***************")

#         if self.request.user.is_anonymous:
#             return serializer.save(owner=anon)
#         return serializer.save(owner=self.request.user)

# class ResponseViewset(viewsets.ModelViewSet):
#     queryset=Response.objects.all()
#     serializer_class=ResponseSerializer
#     lookup_field = 'pk'

# def perform_create(self,serializer):
#         print("***************")
#         print(self.request.user)
#         print("***************")

#         if self.request.user.is_anonymous:
#             return serializer.save(owner=anon)
#         return serializer.save(owner=self.request.user)