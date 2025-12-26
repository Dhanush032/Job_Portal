
from django.shortcuts import render
from django.views import View

class HomeView(View):
    """Home page with job listings"""
    def get(self, request):
        return render(request, 'home.html')

class LoginPageView(View):
    """Login page"""
    def get(self, request):
        return render(request, 'login.html')

class RegisterPageView(View):
    """Registration page"""
    def get(self, request):
        return render(request, 'register.html')

class ProfilePageView(View):
    """User profile page"""
    def get(self, request):
        return render(request, 'profile.html')

class JobDetailPageView(View):
    """Job detail page"""
    def get(self, request, pk):
        return render(request, 'job_detail.html', {'job_id': pk})

class PostJobPageView(View):
    """Post new job page (Employer only)"""
    def get(self, request):
        return render(request, 'post_job.html')

class MyJobsPageView(View):
    """My posted jobs page (Employer only)"""
    def get(self, request):
        return render(request, 'my_jobs.html')

class MyApplicationsPageView(View):
    """My applications page (Job Seeker only)"""
    def get(self, request):
        return render(request, 'my_applications.html')
