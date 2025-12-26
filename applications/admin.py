
from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    
    list_display = ['applicant', 'job', 'status', 'applied_date']
    list_filter = ['status', 'applied_date']
    search_fields = ['applicant__username', 'job__title']
    list_per_page = 20

    readonly_fields = ['applied_date', 'updated_date']
