
from django.db import models
from accounts.models import User

class Job(models.Model):
    

    # Job types
    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    INTERNSHIP = 'internship'
    CONTRACT = 'contract'

    JOB_TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (INTERNSHIP, 'Internship'),
        (CONTRACT, 'Contract'),
    ]

    # Job fields
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default=FULL_TIME)
    salary = models.CharField(max_length=100)  # e.g., "50000-70000" or "Negotiable"
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)

    # Foreign key to employer
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')

    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"

    class Meta:
        ordering = ['-posted_date']
