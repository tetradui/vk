from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, ActivationView, UserListView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', UserListView.as_view()),
    path('profile/', UserProfileView.as_view())
    #path('profile/', ProfileDetail.as_view(), name='profile-detail'),

]