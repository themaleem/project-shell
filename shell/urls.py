from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FeedViewset,CommentListView,CommentDetailView,DiaryListView,DiaryDetailView
router=DefaultRouter()
router.register('feeds',FeedViewset)
urlpatterns = [
    path('comments',CommentListView.as_view(),name=CommentListView.name),
    path('comments/<int:pk>',CommentDetailView.as_view(),name=CommentDetailView.name),
    path('diary',DiaryListView.as_view(),name=DiaryListView.name),
    path('diary/<int:pk>',DiaryDetailView.as_view(),name=DiaryDetailView.name),
]
urlpatterns+= router.urls

