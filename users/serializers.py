from rest_framework import serializers
from .models import Profile,User

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
            ]

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
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
            'date_joined'
            ]