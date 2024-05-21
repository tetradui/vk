from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/', views.ChatListCreateView.as_view()),
    path('api/chat/<int:pk>/', views.ChatDetailView.as_view()),
]
