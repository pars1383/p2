from rest_framework import viewsets, permissions
from .models import JobAd, JobApplication
from .serializers import JobAdSerializer, JobApplicationSerializer

class JobAdViewSet(viewsets.ModelViewSet):
    queryset = JobAd.objects.all()
    serializer_class = JobAdSerializer
    permission_classes = [permissions.AllowAny]

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
