from django.shortcuts import render
from .models import Feed,Comment
from .serializers import FeedSerializer,CommentSerializer,FeedCommentsSerializer

from rest_framework import viewsets,decorators,generics,status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response

# get the anonymous user instance
# to prefill it in post requests
anon=User.objects.get(username='anonymous')

class FeedViewset(viewsets.ModelViewSet):
    queryset=Feed.objects.all()
    serializer_class=FeedSerializer
    lookup_field = 'pk'

    @action(detail=True,methods=["GET"])
    def comments(self,request,pk=None):
        feed=self.get_object()
        serializer_context = {
            'request': request,
        }
        responses=feed.comments
        serializer=CommentSerializer(responses,context=serializer_context,many=True)
        return Response(serializer.data,status=200)

    @action(detail=True,methods=["POST"])
    def comment(self,request,pk=None):
        feed=self.get_object()
        data=request.data
        data['feed'] = feed
        print("******************")
        print(data)
        print("******************")
        data['creator'] = self.request.user.id
        serializer=CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
            

    def perform_create(self,serializer):
        if self.request.user.is_anonymous:
            return serializer.save(author=anon)
        return serializer.save(author=self.request.user)

class CommentListView(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    lookup_field = 'pk'
    name = "comments-list"

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Shows details of a drone per its primary key
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
