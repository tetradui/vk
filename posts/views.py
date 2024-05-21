from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .models import Post
from .serializers import PostSerializers, PostListSerializers
from .permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['author']
    search_fields = ['title']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializers
        return self.serializer_class

    def get_serializer_context(self):
        return {'request': self.request}
   



