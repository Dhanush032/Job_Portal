
from rest_framework import serializers
from .models import Job
from accounts.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    
    posted_by = UserSerializer(read_only=True)
    posted_by_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'company_name', 'location', 'job_type',
            'salary', 'description', 'requirements', 'posted_by',
            'posted_by_id', 'posted_date', 'updated_date', 'is_active'
        ]
        read_only_fields = ['id', 'posted_date', 'updated_date']

    def create(self, validated_data):
        
        request = self.context.get('request')
        validated_data['posted_by'] = request.user
        return super().create(validated_data)


class JobListSerializer(serializers.ModelSerializer):
    
    posted_by_username = serializers.CharField(source='posted_by.username', read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'company_name', 'location', 'job_type', 'salary', 'posted_by_username', 'posted_date', 'is_active']
