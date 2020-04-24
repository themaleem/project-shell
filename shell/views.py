from django.shortcuts import render
from .models import Feed,Comment,Diary
from .serializers import FeedSerializer,CommentSerializer,FeedCommentsSerializer,DiarySerializer

from rest_framework import viewsets,decorators,generics,status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response
from shell import custompermissions
from rest_framework import permissions 
from rest_framework.reverse import reverse
from django_filters import rest_framework as dfilters

class FeedViewset(viewsets.ModelViewSet):
    queryset=Feed.objects.all()
    serializer_class=FeedSerializer
    lookup_field = 'pk'
    filter_fields=(
        'title',
        )
    search_fields=(
        '^title',
        '^body',
        )
        
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
        serializer_context = {
            'request': request,
        }
        data['creator'] = self.request.user.id
        serializer=CommentSerializer(data=data,context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
            

    def perform_create(self,serializer):
        if self.request.user.is_anonymous:
            return serializer.save()
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

class DiaryListView(generics.ListCreateAPIView):
    queryset= Diary.objects.all()
    serializer_class= DiarySerializer
    lookup_field = 'pk'
    name="diary-list"

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly,
        )
   
    # Only authenticated users can create
    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)

class DiaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Diary.objects.all()
    serializer_class= DiarySerializer
    lookup_field = 'pk'
    name="diary-detail"

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly,
        )
