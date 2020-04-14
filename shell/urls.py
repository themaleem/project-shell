from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewset,ResponseViewset
router=DefaultRouter()
router.register('posts',PostViewset)
router.register('responses',ResponseViewset)
urlpatterns = [
    # path('',router.urls)
]
urlpatterns+= router.urls

