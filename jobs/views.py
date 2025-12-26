
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Job
from .serializers import JobSerializer, JobListSerializer


class JobListView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request):
        
        jobs = Job.objects.filter(is_active=True)
        serializer = JobListSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        if not request.user.is_authenticated:
            return Response({
                'error': 'Please login to post a job'
            }, status=status.HTTP_401_UNAUTHORIZED)

        if request.user.role != 'employer':
            return Response({
                'error': 'Only employers can post jobs'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = JobSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Job posted successfully',
                'job': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, pk):
        
        try:
            job = Job.objects.get(pk=pk)
            serializer = JobSerializer(job)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({
                'error': 'Job not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        
        if not request.user.is_authenticated:
            return Response({
                'error': 'Please login'
            }, status=status.HTTP_401_UNAUTHORIZED)

        try:
            job = Job.objects.get(pk=pk)

            
            if job.posted_by != request.user:
                return Response({
                    'error': 'You can only update your own jobs'
                }, status=status.HTTP_403_FORBIDDEN)

            serializer = JobSerializer(job, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Job updated successfully',
                    'job': serializer.data
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Job.DoesNotExist:
            return Response({
                'error': 'Job not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        
        if not request.user.is_authenticated:
            return Response({
                'error': 'Please login'
            }, status=status.HTTP_401_UNAUTHORIZED)

        try:
            job = Job.objects.get(pk=pk)

            
            if job.posted_by != request.user and request.user.role != 'admin':
                return Response({
                    'error': 'You can only delete your own jobs'
                }, status=status.HTTP_403_FORBIDDEN)

            job.delete()
            return Response({
                'message': 'Job deleted successfully'
            }, status=status.HTTP_200_OK)

        except Job.DoesNotExist:
            return Response({
                'error': 'Job not found'
            }, status=status.HTTP_404_NOT_FOUND)


class MyJobsView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if request.user.role != 'employer':
            return Response({
                'error': 'Only employers can view this'
            }, status=status.HTTP_403_FORBIDDEN)

        jobs = Job.objects.filter(posted_by=request.user)
        serializer = JobListSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
