from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, UserSerializer, UserProfileSerializer


User = get_user_model()





@swagger_auto_schema()
class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Вы успешно зарегистрировались', 201)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('Пользователь не найден', 404)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response("Вы успешно активировали аккаунт", 200)
    

# class ProfileDetail(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user.profile
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Получаем данные авторизованного пользователя
        user = request.user
        # Сериализуем данные пользователя
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer