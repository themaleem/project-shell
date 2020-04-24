from rest_framework import viewsets
from .models import Profile,User
from .serializers import UserSerializer,ProfileSerializer
from shell.serializers import DiarySerializer
from django_filters import rest_framework as dfilters  #using this instead of rest_framework.filters.FilterSet
from rest_framework import filters #filters.FilterSet deprecated
from rest_framework.decorators import action
from rest_framework.response import Response

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
    
    @action(detail=True,methods=["GET"])
    def diaries(self,request,pk=None):
        profile=self.get_object()
        serializer_context = {
            'request': request,
        }
        diaries=profile.diaries
        serializer=DiarySerializer(diaries,context=serializer_context,many=True)
        return Response(serializer.data,status=200)

    @action(detail=True,methods=["POST"])
    def diary(self,request,pk=None):
        data=request.data
        serializer_context = {
            'request': request,
        }
        # data['owner'] = self.request.user
        serializer=DiarySerializer(data=data,context=serializer_context)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
            