from rest_framework import viewsets
from .models import Profile,User
from .serializers import UserSerializer,ProfileSerializer
from django_filters import rest_framework as dfilters  #using this instead of rest_framework.filters.FilterSet
from rest_framework import filters #filters.FilterSet deprecated

class UserViewSet(viewsets.ModelViewSet):
    """
    returns list and allow creation of User instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfilesFilter(dfilters.FilterSet):
    """
    profiles username filter class for
    for the Profile model
    """ 

    username = dfilters.AllValuesFilter(field_name='user__username') # user.username field
    class Meta:
        model = Profile
        fields = (
            'username',
            )
class ProfileViewSet(viewsets.ModelViewSet):
    """
    returns list and allow creation of Profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # filter_backends = (dfilters.DjangoFilterBackend,)
    filter_class = ProfilesFilter
    filter_fields=(
        'generated_username', #name of the profiles
        'username'
        )