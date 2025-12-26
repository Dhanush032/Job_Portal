
from django.urls import path
from .views import (
    ApplyJobView,
    MyApplicationsView,
    JobApplicationsView,
    UpdateApplicationStatusView,
    AllApplicationsView
)

urlpatterns = [
    path('apply/', ApplyJobView.as_view(), name='apply-job'),
    path('my-applications/', MyApplicationsView.as_view(), name='my-applications'),
    path('job/<int:job_id>/', JobApplicationsView.as_view(), name='job-applications'),
    path('<int:pk>/status/', UpdateApplicationStatusView.as_view(), name='update-status'),
    path('all/', AllApplicationsView.as_view(), name='all-applications'),
]
