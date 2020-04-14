from rest_framework import serializers
from .models import Post,Draft,Profile,Response


class PostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Response
        fields=[
            'id',
            'body',
        ]

# class ResponseSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=Response
#         fields=[
#             'id',
#             'url',
#             'body',
#             'post_id'
#         ]
class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner= serializers.ReadOnlyField(source="owner.username")
    created_at=serializers.DateTimeField()
    responses=ResponseSerializer(many=True)
    class Meta:
        model= Post
        fields=[
            'id',
            'url',
            'owner',
            'title',
            'created_at',
            'body',
            'responses',
        ]
