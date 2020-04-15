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
        ]