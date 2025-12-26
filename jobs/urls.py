
from django.urls import path
from .views import JobListView, JobDetailView, MyJobsView

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('my-jobs/', MyJobsView.as_view(), name='my-jobs'),
]