from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import toggle_like, CommentViewSet

router = DefaultRouter()
router.register('comment', CommentViewSet)

urlpatterns = [
    path('like/<int:id>/', toggle_like),
    path('', include(router.urls))
]