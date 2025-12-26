
from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'company_name', 'location', 'job_type', 'posted_by', 'is_active', 'posted_date']
    list_filter = ['job_type', 'is_active', 'posted_date']
    search_fields = ['title', 'company_name', 'location']
    list_per_page = 20

    
    readonly_fields = ['posted_date', 'updated_date']
