from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        # Получаем пользователя, совершившего запрос
        user = self.context['request'].user
        # Создаем пост и автоматически устанавливаем его автора
        post = Post.objects.create(author=user, **validated_data)
        return post

    def update(self, instance, validated_data):
        # Убеждаемся, что автор остается неизменным во время обновлений
        return super().update(instance, validated_data)

class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'author', 'title')