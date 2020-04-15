from rest_framework import viewsets
from .models import Profile,User
from .serializers import UserSerializer,ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    returns list and allow creation of User instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileViewSet(viewsets.ModelViewSet):
    """
    returns list and allow creation of Profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
