
from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserLogoutView,
    AllUsersView,
    DeleteUserView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/', AllUsersView.as_view(), name='all-users'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='delete-user'),
]

