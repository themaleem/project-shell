from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FeedViewset
router=DefaultRouter()
router.register('feeds',FeedViewset)
urlpatterns = [
]
urlpatterns+= router.urls

