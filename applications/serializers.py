
from rest_framework import serializers
from .models import Application
from jobs.serializers import JobSerializer
from accounts.serializers import UserSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    
    applicant = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    job_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'job', 'job_id', 'applicant', 'resume',
            'cover_letter', 'status', 'applied_date', 'updated_date'
        ]
        read_only_fields = ['id', 'applicant', 'applied_date', 'updated_date', 'status']

    def create(self, validated_data):
        
        request = self.context.get('request')
        validated_data['applicant'] = request.user
        return super().create(validated_data)

    def validate_job_id(self, value):
        
        from jobs.models import Job
        try:
            Job.objects.get(id=value)
        except Job.DoesNotExist:
            raise serializers.ValidationError("Job does not exist")
        return value


class ApplicationListSerializer(serializers.ModelSerializer):
    
    job_title = serializers.CharField(source='job.title', read_only=True)
    company_name = serializers.CharField(source='job.company_name', read_only=True)
    applicant_name = serializers.CharField(source='applicant.username', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job_title', 'company_name', 'applicant_name', 'status', 'applied_date']
