from django.conf import settings
from django.db import models

class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Chat(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return f"Chat between: {', '.join([user.username for user in self.participants.all()])}"
