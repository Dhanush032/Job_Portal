
from django.urls import path
from .views_frontend import (
    HomeView,
    LoginPageView,
    RegisterPageView,
    ProfilePageView,
    JobDetailPageView,
    PostJobPageView,
    MyJobsPageView,
    MyApplicationsPageView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login-page'),
    path('register/', RegisterPageView.as_view(), name='register-page'),
    path('profile/', ProfilePageView.as_view(), name='profile-page'),
    path('job/<int:pk>/', JobDetailPageView.as_view(), name='job-detail-page'),
    path('post-job/', PostJobPageView.as_view(), name='post-job-page'),
    path('my-jobs/', MyJobsPageView.as_view(), name='my-jobs-page'),
    path('my-applications/', MyApplicationsPageView.as_view(), name='my-applications-page'),
]
