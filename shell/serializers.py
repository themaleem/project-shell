from rest_framework import serializers
from .models import Post,Draft,Profile,Response


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner= serializers.ReadOnlyField(source="owner.username")
    created_at=serializers.DateTimeField()
    class Meta:
        model= Post
        fields=[
            'id',
            'url',
            'owner',
            'title',
            'body',
            'created_at',
        ]