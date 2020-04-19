from rest_framework import serializers
from .models import Profile,User

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Profile
		fields = (
			'url',
			'name'
			)
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'first_name',
            'last_name', 
            'email',
            'profile'
            ]

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    date_joined=serializers.DateTimeField(read_only=True)
    avatar=serializers.ImageField(allow_empty_file=True, use_url=True)
    user_published = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='feed-detail')
    user_drafts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='feed-detail')
    # user_published=FeedSerializer(many=True)
    # user_drafts=FeedSerializer(many=True)
    diaries = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='diary-detail')
    # diaries=DiarySerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'url',
            'user',
            'generated_username', 
            'status', 
            'avatar',
            'one_word_description',
            'date_joined',
            'user_published',
            'user_drafts',
            'diaries',
            ]