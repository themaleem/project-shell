from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


# get the anonymous user instance
# to prefill it in post requests
anon=User.objects.get(username='anonymous')

class PostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field = 'pk'


    def perform_create(self,serializer):
        print("***************")
        print(self.request.user.is_anonymous)
        print("***************")
        
        if self.request.user.is_anonymous:
            return serializer.save(owner=anon)
        return serializer.save(owner=self.request.user)