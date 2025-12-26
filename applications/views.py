
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Application
from jobs.models import Job
from .serializers import ApplicationSerializer, ApplicationListSerializer


class ApplyJobView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        if request.user.role != 'job_seeker':
            return Response({
                'error': 'Only job seekers can apply for jobs'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = ApplicationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({
                    'message': 'Application submitted successfully',
                    'application': serializer.data
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    'error': 'You have already applied for this job'
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyApplicationsView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if request.user.role != 'job_seeker':
            return Response({
                'error': 'Only job seekers can view this'
            }, status=status.HTTP_403_FORBIDDEN)

        applications = Application.objects.filter(applicant=request.user)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JobApplicationsView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, job_id):
        
        if request.user.role != 'employer':
            return Response({
                'error': 'Only employers can view applications'
            }, status=status.HTTP_403_FORBIDDEN)

        try:
            
            job = Job.objects.get(pk=job_id)
            if job.posted_by != request.user:
                return Response({
                    'error': 'You can only view applications for your own jobs'
                }, status=status.HTTP_403_FORBIDDEN)

            applications = Application.objects.filter(job=job)
            serializer = ApplicationSerializer(applications, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Job.DoesNotExist:
            return Response({
                'error': 'Job not found'
            }, status=status.HTTP_404_NOT_FOUND)


class UpdateApplicationStatusView(APIView):
    
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        if request.user.role != 'employer':
            return Response({
                'error': 'Only employers can update application status'
            }, status=status.HTTP_403_FORBIDDEN)

        try:
            application = Application.objects.get(pk=pk)

            
            if application.job.posted_by != request.user:
                return Response({
                    'error': 'You can only update applications for your own jobs'
                }, status=status.HTTP_403_FORBIDDEN)

            
            new_status = request.data.get('status')
            if new_status not in ['pending', 'accepted', 'rejected']:
                return Response({
                    'error': 'Invalid status. Use: pending, accepted, or rejected'
                }, status=status.HTTP_400_BAD_REQUEST)

            application.status = new_status
            application.save()

            return Response({
                'message': 'Application status updated successfully',
                'application': ApplicationSerializer(application).data
            }, status=status.HTTP_200_OK)

        except Application.DoesNotExist:
            return Response({
                'error': 'Application not found'
            }, status=status.HTTP_404_NOT_FOUND)


class AllApplicationsView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if request.user.role != 'admin':
            return Response({
                'error': 'Only admins can view all applications'
            }, status=status.HTTP_403_FORBIDDEN)

        applications = Application.objects.all()
        serializer = ApplicationListSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

