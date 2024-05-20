from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated


from posts.models import Post
from .models import Like, Comment, Favorite
from .serializers import CommentSerializer, FavoriteSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    post = get_object_or_404(Post, id=id)
    if Like.objects.filter(user=user, post=post).exists():
        Like.objects.filter(user=user, post=post).delete()        
    else:
        Like.objects.create(user=user, post=post)
    return Response(201)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in self.permission_classes]
    
class FavoritesViewSet(ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Фильтруем queryset по текущему пользователю
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Автоматически устанавливаем текущего пользователя как владельца
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        post_id = request.data.get('post')
        
        # Проверяем, существует ли пост
        post = get_object_or_404(Post, id=post_id)
        
        # Проверяем, есть ли уже пост в избранных у пользователя
        if Favorite.objects.filter(user=user, post=post).exists():
            return Response({'detail': 'Этот пост уже в вашем избранном.'}, status=401)
        
        # Создаем объект избранного с текущим пользователем
        favorite = Favorite(user=user, post=post)
        favorite.save()
        
        serializer = self.get_serializer(favorite)
        return Response(serializer.data, status=201)