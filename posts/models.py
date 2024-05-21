from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')

    title = models.CharField(max_length=100, verbose_name='Название', blank=True)
    image = models.ImageField(upload_to='posts_img/', verbose_name='Изображение', blank=True)

    description = models.TextField(verbose_name='Описание', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title






