from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,ProfileViewSet
router=DefaultRouter()
router.register('users',UserViewSet)
router.register('profiles',ProfileViewSet)
urlpatterns = [
]
urlpatterns+= router.urls

