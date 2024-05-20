from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import toggle_like, CommentViewSet, FavoritesViewSet

router = DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'favorites', FavoritesViewSet, basename='favorites')

urlpatterns = [
    path('like/<int:id>/', toggle_like),
    path('', include(router.urls)),
]
