from rest_framework import serializers
from .models import Feed,Comment
from taggit_serializer.serializers import TagListSerializerField,TaggitSerializer

class FeedSerializer(TaggitSerializer,serializers.HyperlinkedModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    is_published=serializers.BooleanField(default=False,read_only=True)
    created=serializers.BooleanField(default=False,read_only=True)
    tags = TagListSerializerField()
    # serializer for the category model
    class Meta:
        model = Feed
        fields = [
            'id',
            'url',
            'title',
            'author',
            'body',
            'is_published',
            'created',
            'status',
            'tags',
            'comments_count'
        ]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    feed = serializers.SlugRelatedField(queryset=Feed.objects.all(), slug_field="title")
    created = serializers.DateTimeField(read_only=True)
    active =serializers.BooleanField(default=True,read_only=True)

    class Meta:
        model = Comment
        fields=[
            'id',
            'url',
            'creator',
            'feed',
            'comment_text',
            'created',
            'active'
        ]

class FeedCommentsSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    active =serializers.BooleanField(default=True,read_only=True)

    class Meta:
        model = Comment
        fields=[
            'feed_id',
            'creator',
            'comment_text',
            'created',
            'active'
        ]