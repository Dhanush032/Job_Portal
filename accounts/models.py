from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User Model
    
    """

    # Define user roles
    ADMIN = 'admin'
    EMPLOYER = 'employer'
    JOB_SEEKER = 'job_seeker'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (EMPLOYER, 'Employer'),
        (JOB_SEEKER, 'Job Seeker'),
    ]

    # Additional fields
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=JOB_SEEKER)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    class Meta:
        ordering = ['-created_at']
