from rest_framework import serializers
from .models import Feed,Comment


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    # serializer for the category model
    class Meta:
        model = Feed
        fields = [
            'id',
            'url',
            'title',
            'author',
            'body',
            'tags',
            'status'
        ]