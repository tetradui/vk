from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, ActivationView, UserListView, UserProfileView, UserProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
]
